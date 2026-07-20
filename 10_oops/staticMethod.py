class classUtils:
    @staticmethod
    def cleanIngredients(text):
        return [item.strip() for item in text.split(",")]
    
raw = " water , milk , ginger , honey"

obj = classUtils()
cleaned = classUtils.cleanIngredients(raw)
print(cleaned)