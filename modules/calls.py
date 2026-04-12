"""
Haq - Call Detection Module
"""

SPAM_NUMBERS = ["+96171234567", "+96176854321", "+96176458912"]

def detect_spam_call(phone_number):
    results = {
        "platform": "Call",
        "number": phone_number,
        "is_spam": False,
        "confidence": 0,
        "reason": "",
        "recommendation": ""
    }
    
    if phone_number in SPAM_NUMBERS:
        results["is_spam"] = True
        results["confidence"] = 90
        results["reason"] = "رقم مبلغ عنه"
        results["recommendation"] = "🚨 لا ترد، احظر الرقم"
    else:
        results["is_spam"] = False
        results["confidence"] = 20
        results["reason"] = "رقم غير معروف"
        results["recommendation"] = "⚠️ كن حذراً، لا تشارك معلومات"
    
    return results
