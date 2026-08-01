from lm_eval.tasks import TaskManager

task_manager = TaskManager()
loaded = task_manager.load(["gsm8k"])

# Retrieve the GSM8k task instance
gsm8k_task = loaded["tasks"]["gsm8k"]

# Print dataset split counts
eval_docs = gsm8k_task.eval_docs
fewshot_docs = gsm8k_task.fewshot_docs()

print(f"Evaluation samples (test set): {len(eval_docs)}")
print(f"Few-shot prompt pool (train set): {len(fewshot_docs) if fewshot_docs else 0}")