text = """

Dette er første luke i Novacare sin kodekalender!

Vi arrang🐘r🐘r kod🐘kal🐘nd🐘r to gang🐘r i år🐘t, båd🐘 påsk🐘 og adv🐘nt! Hv🐘r d🦓g til og m🐘d 24. d🐘s🐘mb🐘r komm🐘r d🐘t 🐘n oppg🦓v🐘 som på 🐘n 🐘ll🐘r 🦓nn🐘n måt🐘 🐘r r🐘l🦓t🐘rt til kod🐘.

D🐘 først🐘 d🦓g🐘n🐘 k🐖mm🐘r 🐖ppg🦓v🐘n🐘 til å vær🐘 s🐭kt 🐘nkl🐘, 🐖g st🐖rt s🐘tt 🦓ll🐘 s🐖m g🦔ør 🐘t f🐖rsøk vil kl🦓r🐘 å løs🐘 🐖ppg🦓v🐘n🐘. 🐘tt🐘r hv🐘rt vil v🦓nsk🐘ligh🐘tsgr🦓d🐘n øk🐘, 🐖g d🐘t 🐘r ikk🐘 sikk🐘rt 🦓ll🐘 l🐘ng🐘r kl🦓r🐘r 🦓ll🐘 🐖ppg🦓v🐘n🐘. Slik sk🦓l d🐘t vær🐘!

H🦓n s🐖m l🦓g🐘r 🐖ppg🦓🦄🐘n🐘, T🐖m🦓🐌, 🐌t🐖l🐘🐴 ikk🐘 på n🐖🐘n! 🐌å ing🐘n h🦓🐴 fått l🐖🦄 til å l🐘🐌🐘 k🐖🐴🐴🐘ktu🐴 på 🐖ppg🦓🦄🐘n🐘, 🐘ll🐘🐴 🐌🦔🐘kk🐘 🦓t d🐘 f🦓kti🐌k l🦓🐴 🐌🐘g lø🐌🐘. D🐘🐴f🐖🐴 🐘🐴 k🦓n🐌k🦔🐘 T🐖m🦓🐌 d🐘n 🐌🐖m 🐘🐴 🦓ll🐘🐴 m🐘🐌t 🐌p🐘nt på 🐖m n🐖🐘n kl🦓🐴🐘🐴 å lø🐌🐘 🐖ppg🦓🦄🐘n🐘.

H🦄🐘🐴 d🦓g gå🐴 🐖🐵🐵g🦓🦄🐘n ut 🐵å å f🦜🦏🦏🐘 🐘t 🐐🐖d🐘🐖🐴d, 🐖g d🦓g🐘🦏🐌 🐐🐖d🐘🐖🐴d 🐌tå🐴 🐵å 🐌🦜🐌t🐘 l🦜🦏🦔🐘 🦜 d🐘🦏🦏🐘 t🐘🐐🐌t🐘🦏. Du må b🦓🐴🐘 🐌🐘 f🐖🐴b🦜 🦓ll🐘 🐘m🐖🦔🦜🐘🦏🐘, f🐖🐴 d🐘t 🐘🐴 🦜🦏g🐘🦏 🐘m🐖🦔🦜🐘🐴 🦜 🐐🐖🐫🐘🐖🐴🐫🐘t.

🐫🦓g🐘🦏🐌 🐐🐖🐫🐘🐖🐴🐫 🐘🐴:
🐴🐘🦜🦏🐌🐫🐭🐴🐘🐐🦄🦜🐵🦓🐌🦔🐘
"""

emoji_dict = {
        128024 : 'e',
        129427 : 'a',
        128022 : 'o',
        129428 : 'j',
        128045 : 'y',
        128012 : 's',
        128052 : 'r',
        129412 : 'v',
        128053 : 'p',
        129436 : 'i',
        129423 : 'n',
        128016 : 'k',
        128043 : 'd'
    }

translated_text = ""
for i in text:
    if ord(i) in emoji_dict:
        translated_text += emoji_dict[ord(i)]
    else:
        translated_text += i 

print(translated_text)


