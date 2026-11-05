import unittest,math
from ndcg_tie_bounds.core import run
class DomainTests(unittest.TestCase):
 def test_cutoff_tie(self):
  x=run({'k':1,'documents':[dict(id='a',score=1,relevance=3),dict(id='b',score=1,relevance=0)]});self.assertEqual([x['ndcg_min'],x['ndcg_max'],x['ndcg_expected_uniform_ties']],[0,1,.5])
 def test_no_tie(self):
  x=run({'k':2,'documents':[dict(id='a',score=2,relevance=2),dict(id='b',score=1,relevance=1)]});self.assertEqual(x['ndcg_min'],1);self.assertEqual(x['ndcg_max'],1)
 def test_no_gain_unknown(self):self.assertIsNone(run({'documents':[dict(id='a',score=1,relevance=0)]})['ndcg_max'])
