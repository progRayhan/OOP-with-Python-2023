# এখন পর্যন্ত আমি যতগুলো object তৈরি করেছি, সেটার ভিতরে class attribute এর কোন value ই দেইনাই ।
# value pass করার জন্য, আমি একটি set_value নামে method নিয়েছি, সেটা একটা extra কাজ । আমি চাইলে
# extra method টি বাদ দিয়ে, object এর ভিতরই value গুলো বলে দিতে পারি । এক্ষেত্রে আমাকে
# constructor ব্যাবহার করতে হবে ।

# constructor হচ্ছে special type of method, যেটাকে extra ভাবে call দিতে হয়না ।

class Student:
    roll = ""
    gpa = ""

    # constructor
    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa