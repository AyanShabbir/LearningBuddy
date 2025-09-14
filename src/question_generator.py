from transformers import pipeline

class QuestionGenerator:
    def __init__(self, model_name="gpt2"):
        # Load generator once
        self.generator = pipeline("text-generation", model=model_name)
        # Use eos token for padding (avoids warning)
        self.pad_token_id = self.generator.tokenizer.eos_token_id

    def generate_mcq(self, text):
        prompt = f"Generate a multiple choice question with 4 options from: {text}"
        return self.generator(
            prompt,
            max_new_tokens=80,            # replaces max_length
            num_return_sequences=1,
            truncation=True,
            pad_token_id=self.pad_token_id
        )[0]['generated_text']

    def generate_short(self, text):
        prompt = f"Generate a short-answer question from: {text}"
        return self.generator(
            prompt,
            max_new_tokens=50,
            num_return_sequences=1,
            truncation=True,
            pad_token_id=self.pad_token_id
        )[0]['generated_text']

    def generate_open(self, text):
        prompt = f"Generate an open-ended discussion question from: {text}"
        return self.generator(
            prompt,
            max_new_tokens=60,
            num_return_sequences=1,
            truncation=True,
            pad_token_id=self.pad_token_id
        )[0]['generated_text']

    def generate_all(self, text):
        return {
            "mcq": self.generate_mcq(text),
            "short": self.generate_short(text),
            "open": self.generate_open(text)
        }

if __name__ == "__main__":
    qg = QuestionGenerator()
    sample = "Photosynthesis is how green plants make food using sunlight, water, and air."
    print(qg.generate_all(sample))
