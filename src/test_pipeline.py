from pipeline import analyze_review

review = """
The motor stopped working after two weeks.
Customer support refused the warranty claim.
Very disappointed with the product quality.
"""

result = analyze_review(review, "Electronics")

for k,v in result.items():
    print(k,":",v)