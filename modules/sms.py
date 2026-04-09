"""
Haq - SMS Detection Module
"""

def detect_sms_spam(sender, message, language="ar"):
    results = {
        "platform": "SMS",
        "sender": sender,
        "message": message,
        "is_spam": False,
        "confidence": 0,
        "reasons": [],
        "recommendation": "",
        "type": None
    }
    
    suspicious_keywords = ["ربحت", "جائزة", "فزت", "بنك", "حساب", "مجمّد", "عاجل", "تحقق", "أمني", "أمان"]
    
    for keyword in suspicious_keywords:
        if keyword in message:
            results["is_spam"] = True
            results["confidence"] = 70
            results["reasons"].append(f"يحتوي على كلمة: {keyword}")
            results["type"] = "احتيال"
    
    if "http://" in message or "https://" in message:
        results["is_spam"] = True
        results["confidence"] = max(results["confidence"], 80)
        results["reasons"].append("يحتوي على رابط مشبوه")
    
    if results["is_spam"]:
        results["recommendation"] = "⚠️ لا ترد، لا تنقر على الرابط، احذف الرسالة"
    else:
        results["recommendation"] = "✅ تبدو آمنة، كن حذراً"
    
    return results
