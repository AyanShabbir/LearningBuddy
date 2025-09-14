import random

class LearningPath:
    def __init__(self, study_materials):
        """
        study_materials: dict like {topic: [easy, medium, hard]}
        """
        self.materials = study_materials

    def recommend_next(self, topic, score):
        """
        score: int 0-100 (quiz score)
        Returns: recommended material
        """
        if score < 40:
            return self.materials[topic][0]  # easy
        elif score < 70:
            return self.materials[topic][1]  # medium
        else:
            return self.materials[topic][2]  # hard

if __name__ == "__main__":
    materials = {
        "photosynthesis": [
            "Plants make food using sun, air, and water. (Easy)",
            "Plants use sunlight, water, and carbon dioxide for photosynthesis. (Medium)",
            "Photosynthesis involves light-dependent and light-independent reactions. (Hard)"
        ]
    }

    lp = LearningPath(materials)
    print(lp.recommend_next("photosynthesis", random.randint(0, 100)))
