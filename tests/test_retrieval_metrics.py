import unittest

from examples.retrieval_metrics import evaluate_ranking


class RetrievalMetricsTests(unittest.TestCase):
    def test_perfect_graded_ranking(self):
        scores = evaluate_ranking(["a", "b"], {"a": 3, "b": 1}, 2)
        self.assertTrue(all(value == 1.0 for value in scores.values()))

    def test_hit_and_recall_measure_different_things(self):
        scores = evaluate_ranking(["x", "a"], {"a": 1, "b": 1}, 2)
        self.assertEqual(scores["hit"], 1.0)
        self.assertEqual(scores["recall"], 0.5)
        self.assertEqual(scores["reciprocal_rank"], 0.5)

    def test_duplicates_do_not_inflate_scores_or_shift_ranks(self):
        repeated = evaluate_ranking(["x", "x", "a"], {"a": 1}, 3)
        self.assertEqual(repeated["reciprocal_rank"], 1.0 / 3)
        self.assertEqual(repeated["ndcg"], 0.5)
        positives = evaluate_ranking(["a", "a", "a"], {"a": 1, "b": 1}, 3)
        self.assertEqual(positives["recall"], 0.5)
        self.assertEqual(positives["precision"], 1.0 / 3)
        self.assertLess(positives["ndcg"], 1.0)

    def test_missing_results_still_use_k_for_precision(self):
        scores = evaluate_ranking(["a"], {"a": 1}, 3)
        self.assertEqual(scores["precision"], 1.0 / 3)
        self.assertEqual(scores["recall"], 1.0)

    def test_cutoff_excludes_late_relevance(self):
        scores = evaluate_ranking(["x", "a"], {"a": 1}, 1)
        self.assertTrue(all(value == 0.0 for value in scores.values()))

    def test_empty_or_unjudged_results(self):
        for ranking, labels in (([], {"a": 1}), (["a"], {}), (["a"], {"a": 0})):
            with self.subTest(ranking=ranking, labels=labels):
                self.assertTrue(all(value == 0.0 for value in evaluate_ranking(ranking, labels, 3).values()))

    def test_reversed_graded_ranking_is_penalized(self):
        scores = evaluate_ranking(["b", "a"], {"a": 3, "b": 1}, 2)
        self.assertEqual(scores["recall"], 1.0)
        self.assertGreater(scores["ndcg"], 0.0)
        self.assertLess(scores["ndcg"], 1.0)

    def test_invalid_cutoffs_and_grades(self):
        for cutoff in (0, -1, 1.5, True):
            with self.subTest(cutoff=cutoff), self.assertRaises(ValueError):
                evaluate_ranking([], {}, cutoff)
        for grade in (-1, 4, 0.5, True):
            with self.subTest(grade=grade), self.assertRaises(ValueError):
                evaluate_ranking(["a"], {"a": grade}, 1)


if __name__ == "__main__":
    unittest.main()
