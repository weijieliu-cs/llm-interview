import math
import unittest

from examples.attention import scaled_dot_product_attention, stable_softmax


class AttentionTests(unittest.TestCase):
    def setUp(self):
        self.q = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
        self.k = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
        self.v = [[10.0, 0.0], [0.0, 10.0], [5.0, 5.0]]

    def test_softmax_large_logits_and_mask(self):
        weights = stable_softmax([10000.0, 10000.0, -math.inf])
        self.assertEqual(weights, [0.5, 0.5, 0.0])

    def test_invalid_softmax_rows(self):
        for row in ([], [-math.inf, -math.inf], [math.nan], [math.inf]):
            with self.subTest(row=row), self.assertRaises(ValueError):
                stable_softmax(row)

    def test_causal_future_cannot_change_prefix(self):
        original, weights = scaled_dot_product_attention(self.q, self.k, self.v, causal=True)
        changed_keys = self.k[:2] + [[100.0, -100.0]]
        changed_values = self.v[:2] + [[-900.0, 900.0]]
        changed, _ = scaled_dot_product_attention(self.q, changed_keys, changed_values, causal=True)
        self.assertEqual(original[:2], changed[:2])
        self.assertEqual(original[0], self.v[0])
        for row_index, row in enumerate(weights):
            self.assertAlmostEqual(sum(row), 1.0)
            self.assertTrue(all(x == 0.0 for x in row[row_index + 1:]))

    def test_noncausal_attention_uses_later_values(self):
        original, _ = scaled_dot_product_attention(self.q, self.k, self.v)
        changed, _ = scaled_dot_product_attention(self.q, self.k, self.v[:2] + [[100.0, 100.0]])
        self.assertNotEqual(original[0], changed[0])

    def test_incremental_queries_match_full_causal_pass(self):
        full, _ = scaled_dot_product_attention(self.q, self.k, self.v, causal=True)
        for position in range(len(self.q)):
            output, _ = scaled_dot_product_attention(
                [self.q[position]], self.k[:position + 1], self.v[:position + 1],
                causal=True, query_start=position,
            )
            for actual, expected in zip(output[0], full[position]):
                self.assertAlmostEqual(actual, expected)

    def test_uniform_scores_average_values_and_allow_other_value_width(self):
        output, _ = scaled_dot_product_attention([[0.0]], [[1.0], [2.0]], [[2.0, 4.0], [6.0, 8.0]])
        self.assertEqual(output, [[4.0, 6.0]])

    def test_invalid_matrices(self):
        inputs = [
            ([], self.k, self.v),
            ([[1.0], [1.0, 2.0]], self.k, self.v),
            ([[1.0]], self.k, self.v),
            (self.q, self.k, self.v[:1]),
            ([[math.nan, 0.0]], self.k, self.v),
        ]
        for query, key, value in inputs:
            with self.subTest(query=query), self.assertRaises(ValueError):
                scaled_dot_product_attention(query, key, value)

    def test_invalid_query_offset(self):
        for offset in (-1, 0.5, True):
            with self.subTest(offset=offset), self.assertRaises(ValueError):
                scaled_dot_product_attention(self.q, self.k, self.v, query_start=offset)


if __name__ == "__main__":
    unittest.main()
