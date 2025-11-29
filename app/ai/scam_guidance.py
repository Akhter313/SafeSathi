# app/ai/scam_guidance.py

import os

def detect_scam_type(text: str) -> str:
    """
    Analyzes the text for keywords to determine the type of scam.
    Returns one of: "bank", "job", "parcel", "investment", "loan", "social", "generic"
    """
    text = text.lower()

    # Keywords for different scam types
    keywords = {
        "bank": ["otp", "kyc", "bank", "upi", "account", "blocking", "limit", "verification", "debit", "credit", "card"],
        "job": ["job", "salary", "work from home", "part-time", "hr", "offer letter", "hiring", "recruit"],
        "parcel": ["parcel", "courier", "custom", "shipment", "delivery", "package", "pending charges", "address"],
        "investment": ["investment", "crypto", "bitcoin", "stock", "profit", "doubles money", "returns", "trading"],
        "loan": ["loan", "instant", "repay", "interest", "threat", "contacts", "gallery", "harass"],
        "social": ["instagram", "facebook", "whatsapp", "hacked", "login", "code", "verification code", "account takeover"]
    }

    # Check for matches
    for scam_type, words in keywords.items():
        if any(word in text for word in words):
            return scam_type

    return "generic"

def generate_scam_guidance(text: str, label: str, scam_type: str, lang: str = "en") -> str:
    """
    Generates a structured guidance message based on the scam type and label.
    """
    
    # Templates for guidance
    if lang == "hi":
        templates = {
            "bank": (
                "بैंक / KYC / UPI स्कैम का पता चला\n\n"
                "तत्काल कदम:\n"
                "1. अपना कार्ड/खाता तुरंत ब्लॉक करें अपने बैंक की ऐप या कस्टमर केयर के माध्यम से।\n"
                "2. OTP किसी के साथ साझा न करें, भले ही वे बैंक अधिकारी होने का दावा करें।\n"
                "3. यदि पैसे कट गए हैं, तो वित्तीय धोखाधड़ी की रिपोर्ट करने के लिए तुरंत 1930 पर कॉल करें।\n"
                "4. अपना UPI PIN और नेटबैंकिंग पासवर्ड बदलें।"
            ),
            "job": (
                "नकली नौकरी / टास्क स्कैम का पता चला\n\n"
                "तत्काल कदम:\n"
                "1. पैसे देना बंद करें। वैध नौकरियां कभी भी प्रशिक्षण या पंजीकरण के लिए भुगतान नहीं मांगती हैं।\n"
                "2. संपर्क को ब्लॉक करें WhatsApp/Telegram पर।\n"
                "3. अपने बैंक विवरण या ID प्रमाण साझा न करें।\n"
                "4. उस प्लेटफॉर्म पर नौकरी पोस्टिंग की रिपोर्ट करें जहां आपने इसे पाया।"
            ),
            "parcel": (
                "पार्सल / कस्टम्स स्कैम का पता चला\n\n"
                "तत्काल कदम:\n"
                "1. कोई 'कस्टम्स' या 'डिलीवरी' शुल्क न दें।\n"
                "2. आधिकारिक कूरियर वेबसाइट पर ट्रैकिंग नंबर सत्यापित करें।\n"
                "3. 'पुलिस कार्रवाई' या 'गिरफ्तारी' की धमकियों को अनदेखा करें - ये नकली रणनीतियां हैं।\n"
                "4. नंबर को ब्लॉक करें।"
            ),
            "investment": (
                "निवेश / क्रिप्टो स्कैम का पता चला\n\n"
                "तत्काल कदम:\n"
                "1. निवेश करना बंद करें। 'पैसे दोगुने' करने का वादा करने वाली योजनाएं हमेशा स्कैम होती हैं।\n"
                "2. जो भी धन आप निकाल सकते हैं, निकालें (यदि संभव हो)।\n"
                "3. प्लेटफॉर्म की रिपोर्ट 1930 को करें।\n"
                "4. 'रिकवरी एजेंटों' पर भरोसा न करें जो शुल्क के लिए आपके पैसे वापस दिलाने का दावा करते हैं।"
            ),
            "loan": (
                "तत्काल लोन ऐप स्कैम का पता चला\n\n"
                "तत्काल कदम:\n"
                "1. ऐप को तुरंत अनइंस्टॉल करें।\n"
                "2. ऐप अनुमतियां रद्द करें (कैमरा, संपर्क, स्टोरेज) अपने फोन सेटिंग्स से।\n"
                "3. अपने संपर्कों को सूचित करें कि आपका फोन हैक हो गया था।\n"
                "4. Google Play Store और साइबर अपराध पोर्टल पर ऐप की रिपोर्ट करें।"
            ),
            "social": (
                "सोशल मीडिया / अकाउंट टेकओवर का पता चला\n\n"
                "तत्काल कदम:\n"
                "1. अपना पासवर्ड रीसेट करने का प्रयास करें ईमेल/SMS का उपयोग करके।\n"
                "2. सुरक्षा सेटिंग्स से सभी सत्रों से लॉग आउट करें।\n"
                "3. Two-Factor Authentication (2FA) सक्षम करें।\n"
                "4. अपने दोस्तों को चेतावनी दें कि आपके खाते से भेजे गए लिंक पर क्लिक न करें।"
            ),
            "generic": (
                "संदिग्ध गतिविधि का पता चला\n\n"
                "तत्काल कदम:\n"
                "1. व्यक्तिगत जानकारी साझा न करें (OTP, पासवर्ड, PIN)।\n"
                "2. यदि आपने पैसे खो दिए हैं, तो 1930 पर कॉल करें।\n"
                "3. संदिग्ध नंबर/संपर्क को ब्लॉक करें।\n"
                "4. मजबूत पासवर्ड के साथ अपने खातों को सुरक्षित करें।"
            )
        }
    elif lang == "ur":
        templates = {
            "bank": (
                "بینک / KYC / UPI اسکام کا پتہ چلا\n\n"
                "فوری اقدامات:\n"
                "1. اپنا کارڈ/اکاؤنٹ فوری طور پر بلاک کریں اپنے بینک کی ایپ یا کسٹمر کیئر کے ذریعے۔\n"
                "2. OTP کسی کے ساتھ شیئر نہ کریں، چاہے وہ بینک اہلکار ہونے کا دعویٰ کریں۔\n"
                "3. اگر پیسے کٹ گئے ہیں، تو مالی دھوکہ دہی کی رپورٹ کرنے کے لیے فوراً 1930 پر کال کریں۔\n"
                "4. اپنا UPI PIN اور نیٹ بینکنگ پاس ورڈ تبدیل کریں۔"
            ),
            "job": (
                "جعلی نوکری / ٹاسک اسکام کا پتہ چلا\n\n"
                "فوری اقدامات:\n"
                "1. پیسے دینا بند کریں۔ جائز نوکریاں کبھی بھی تربیت یا رجسٹریشن کے لیے ادائیگی نہیں مانگتیں۔\n"
                "2. رابطہ کو بلاک کریں WhatsApp/Telegram پر۔\n"
                "3. اپنے بینک تفصیلات یا ID ثبوت شیئر نہ کریں۔\n"
                "4. اس پلیٹ فارم پر نوکری کی پوسٹنگ کی رپورٹ کریں جہاں آپ نے اسے پایا۔"
            ),
            "parcel": (
                "پارسل / کسٹمز اسکام کا پتہ چلا\n\n"
                "فوری اقدامات:\n"
                "1. کوئی 'کسٹمز' یا 'ڈیلیوری' فیس ادا نہ کریں۔\n"
                "2. سرکاری کوریئر ویب سائٹ پر ٹریکنگ نمبر کی تصدیق کریں۔\n"
                "3. 'پولیس کارروائی' یا 'گرفتاری' کی دھمکیوں کو نظر انداز کریں - یہ جعلی حربے ہیں۔\n"
                "4. نمبر کو بلاک کریں۔"
            ),
            "investment": (
                "سرمایہ کاری / کرپٹو اسکام کا پتہ چلا\n\n"
                "فوری اقدامات:\n"
                "1. سرمایہ کاری بند کریں۔ 'پیسے دوگنے' کرنے کا وعدہ کرنے والی سکیمیں ہمیشہ اسکام ہوتی ہیں۔\n"
                "2. جو بھی رقم آپ نکال سکتے ہیں، نکالیں (اگر ممکن ہو)۔\n"
                "3. پلیٹ فارم کی رپورٹ 1930 کو کریں۔\n"
                "4. 'ریکوری ایجنٹوں' پر بھروسہ نہ کریں جو فیس کے لیے آپ کے پیسے واپس دلانے کا دعویٰ کرتے ہیں۔"
            ),
            "loan": (
                "فوری قرض ایپ اسکام کا پتہ چلا\n\n"
                "فوری اقدامات:\n"
                "1. ایپ کو فوری طور پر ان انسٹال کریں۔\n"
                "2. ایپ کی اجازتیں منسوخ کریں (کیمرہ، رابطے، اسٹوریج) اپنے فون کی ترتیبات سے۔\n"
                "3. اپنے رابطوں کو مطلع کریں کہ آپ کا فون ہیک ہو گیا تھا۔\n"
                "4. Google Play Store اور سائبر کرائم پورٹل پر ایپ کی رپورٹ کریں۔"
            ),
            "social": (
                "سوشل میڈیا / اکاؤنٹ ٹیک اوور کا پتہ چلا\n\n"
                "فوری اقدامات:\n"
                "1. اپنا پاس ورڈ ری سیٹ کرنے کی کوشش کریں ای میل/SMS استعمال کرکے۔\n"
                "2. سیکیورٹی ترتیبات سے تمام سیشنز سے لاگ آؤٹ کریں۔\n"
                "3. Two-Factor Authentication (2FA) فعال کریں۔\n"
                "4. اپنے دوستوں کو خبردار کریں کہ آپ کے اکاؤنٹ سے بھیجے گئے لنکس پر کلک نہ کریں۔"
            ),
            "generic": (
                "مشکوک سرگرمی کا پتہ چلا\n\n"
                "فوری اقدامات:\n"
                "1. ذاتی معلومات شیئر نہ کریں (OTP، پاس ورڈ، PIN)۔\n"
                "2. اگر آپ نے پیسے کھو دیے ہیں، تو 1930 پر کال کریں۔\n"
                "3. مشکوک نمبر/رابطہ کو بلاک کریں۔\n"
                "4. مضبوط پاس ورڈز کے ساتھ اپنے اکاؤنٹس کو محفوظ کریں۔"
            )
        }
    else:  # English templates
        templates = {
            "bank": (
                "Bank / KYC / UPI Scam Detected\n\n"
                "Immediate Steps:\n"
                "1. Block your card/account immediately via your bank's app or customer care.\n"
                "2. Do NOT share OTPs with anyone, even if they claim to be bank officials.\n"
                "3. If money was deducted, call 1930 immediately to report financial fraud.\n"
                "4. Change your UPI PIN and netbanking password."
            ),
            "job": (
                "Fake Job / Task Scam Detected\n\n"
                "Immediate Steps:\n"
                "1. Stop paying money. Legitimate jobs never ask you to pay for training or registration.\n"
                "2. Block the contact on WhatsApp/Telegram.\n"
                "3. Do not share your bank details or ID proofs.\n"
                "4. Report the job posting on the platform where you found it."
            ),
            "parcel": (
                "Parcel / Customs Scam Detected\n\n"
                "Immediate Steps:\n"
                "1. Do not pay any 'customs' or 'delivery' fees.\n"
                "2. Verify the tracking number on the official courier website (e.g., India Post, BlueDart).\n"
                "3. Ignore threats of 'police action' or 'arrest' - these are fake tactics.\n"
                "4. Block the number."
            ),
            "investment": (
                "Investment / Crypto Scam Detected\n\n"
                "Immediate Steps:\n"
                "1. Stop investing. Schemes promising 'double money' are always scams.\n"
                "2. Withdraw whatever funds you can (if possible).\n"
                "3. Report the platform to 1930.\n"
                "4. Do not trust 'recovery agents' who claim they can get your money back for a fee."
            ),
            "loan": (
                "Instant Loan App Scam Detected\n\n"
                "Immediate Steps:\n"
                "1. Uninstall the app immediately.\n"
                "2. Revoke app permissions (Camera, Contacts, Storage) from your phone settings.\n"
                "3. Inform your contacts that your phone was hacked and to ignore messages from scammers.\n"
                "4. Report the app to the Google Play Store and Cybercrime portal."
            ),
            "social": (
                "Social Media / Account Takeover Detected\n\n"
                "Immediate Steps:\n"
                "1. Try to reset your password using email/SMS immediately.\n"
                "2. Log out of all sessions from security settings.\n"
                "3. Enable Two-Factor Authentication (2FA).\n"
                "4. Warn your friends not to click links sent from your account."
            ),
            "generic": (
                "Suspicious Activity Detected\n\n"
                "Immediate Steps:\n"
                "1. Do not share personal info (OTP, Passwords, PINs).\n"
                "2. If you lost money, call 1930.\n"
                "3. Block the suspicious number/contact.\n"
                "4. Secure your accounts with strong passwords."
            )
        }

    # Select guidance
    guidance = templates.get(scam_type, templates["generic"])

    # Add specific note if the model thinks it's NOT a scam but we detected keywords
    if label == "not_scam" and scam_type != "generic":
        guidance = (
            "ℹ️ **Note:** Our automated check didn't flag this as a typical scam text, "
            "but your story mentions keywords related to **" + scam_type.upper() + "** scams.\n"
            "Please follow these precautions just in case:\n\n" + guidance
        )
    elif label == "not_scam" and scam_type == "generic":
        guidance = (
            "✅ **Analysis:** This doesn't strongly look like a known scam pattern based on your description.\n"
            "However, always stay cautious. If you are unsure, do not proceed with any transaction.\n\n"
            "**General Safety Tips:**\n"
            "- Never share OTPs.\n"
            "- Verify links before clicking.\n"
            "- Use official apps only."
        )

    # Add evidence reminder
    if lang == "hi":
        evidence_note = (
            "\n\nसबूत सहेजें:\n"
            "स्क्रीनशॉट, चैट हिस्ट्री, ट्रांजैक्शन ID और फोन नंबर सहेजें। रिपोर्ट करने के लिए आपको इनकी जरूरत होगी।"
        )
    elif lang == "ur":
        evidence_note = (
            "\n\nثبوت محفوظ کریں:\n"
            "اسکرین شاٹس، چیٹ ہسٹری، ٹرانزیکشن ID اور فون نمبر محفوظ کریں۔ رپورٹ کرنے کے لیے آپ کو ان کی ضرورت ہوگی۔"
        )
    else:
        evidence_note = (
            "\n\nKeep Evidence:\n"
            "Save screenshots, chat history, transaction IDs, and phone numbers. You will need these for reporting."
        )

    return guidance + evidence_note
