import sys
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer


def translate():
    model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_1.2B").to("cuda")
    tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_1.2B", src_lang="en")
    for line in sys.stdin:
        input_words = line.strip().split()
        if len(input_words) == 0:
            print("")
        else:
            inputs = tokenizer(line, return_tensors="pt")
            translated_tokens = model.generate(input_ids=inputs["input_ids"].to("cuda"),
                                               attention_mask=inputs["attention_mask"].to("cuda"),
                                               forced_bos_token_id=tokenizer.lang_code_to_id["es"])
            print(tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0])


if __name__ == "__main__":
    translate()
