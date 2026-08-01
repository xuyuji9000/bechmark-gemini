Run `lm-eval` against gemini-3.6-flash .

Get start with `gsm8k` task


# Commands
``` shell
lm-eval ls tasks | grep gsm8k

# get counts
python3 count-gsm8k.py
```

``` shell
export GEMINI_API_KEY="your-gemini-api-key"

time lm-eval                                                  \
--model litellm                                               \
--model_args model=gemini/gemini-3.6-flash,num_concurrent=100 \
--tasks gsm8k                                                 \
--num_fewshot 5                                               \
--batch_size 1                                                \
--apply_chat_template                                         \
--output_path ./results_gemini_3_6_flash
```

