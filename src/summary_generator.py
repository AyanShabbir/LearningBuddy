from transformers import pipeline

class SummaryGenerator:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text, level="simple"):
        if level == "simple":
            max_len, min_len = 40, 15
        elif level == "medium":
            max_len, min_len = 80, 30
        else:  # advanced
            max_len, min_len = 120, 60

        summary = self.summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
        return summary[0]['summary_text']

if __name__ == "__main__":
    sg = SummaryGenerator()
    sample = "Photosynthesis is the process by which green plants and some organisms use sunlight..."
    print("Simple:", sg.summarize(sample, "simple"))
    print("Medium:", sg.summarize(sample, "medium"))
    print("Advanced:", sg.summarize(sample, "advanced"))
