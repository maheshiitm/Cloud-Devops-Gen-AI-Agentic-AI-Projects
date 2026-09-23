from evals.evaluator import load_cases,evaluate_case
from app.main import orchestrator

if __name__=="__main__":
    results=[evaluate_case(c,orchestrator) for c in load_cases()]
    for r in results: print(r)
    print("Average:",sum(r["score"] for r in results)/len(results))
