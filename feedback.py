# feedback.py

def show_feedback(is_correct, feedback_texts):
    if is_correct:
        print("\n✅ " + feedback_texts[0])
    else:
        print("\n❌ " + feedback_texts[1])
