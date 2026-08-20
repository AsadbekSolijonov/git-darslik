# Git va GitHub — mashq repozitoriysi

Bu repo [solijonov.uz](https://solijonov.uz/writing/) saytidagi **"Git va GitHub"**
darsliklar seriyasi uchun. Seriyada nima qilingan bo'lsa, hammasi shu yerda —
o'ylab topilgan misollar emas, haqiqiy tarix.

Ya'ni darslikda `git log` chiqishini ko'rsatsam, siz shu yerga kirib o'sha
commitning o'zini ochib ko'rishingiz mumkin.

## Nima ustida ishlaymiz

`xarajat` — kunlik xarajatlarni yozib boradigan kichik Python skript. Loyihaning
o'zi soddagina, chunki bu yerda maqsad — dastur emas, Git.

Lekin u ataylab shunday tanlangan: ichida virtual muhit ham, Python hosil
qiladigan `__pycache__` ham, ma'lumot fayli ham, sir saqlanadigan `.env` ham
bo'ladi. Ya'ni `.gitignore` darsiga kelganda to'rt xil sababni bitta loyihada
ko'rasiz.

## Bu yerdan qanday foydalanish kerak

Darslikni o'qib, buyruqlarni **o'z kompyuteringizda** yozib boring. Bu repo —
tekshirish uchun: adashib qolsangiz yoki "menda boshqacha chiqdi" desangiz,
shu yerni ochib solishtirasiz.

Har qismning oxirgi holati tag bilan belgilangan:

```bash
git clone https://github.com/AsadbekSolijonov/git-darslik.git
cd git-darslik
git tag                    # qaysi qismlar bor
git checkout qism-2        # 2-qism tugagandagi holat
git switch main            # oxirgi holatga qaytish
```

Branchlar ham ataylab o'chirilmagan. Darslikda branch ochib, merge qilib,
conflict yaratgan bo'lsak — o'sha branchlar shu yerda turibdi:

```bash
git branch -a              # barcha branchlar, remote'dagilari bilan
```

## Darsliklar

Seriya chiqa boshlagach ro'yxat shu yerga qo'shiladi.

---

Savol yoki xato topsangiz — [Issue oching](https://github.com/AsadbekSolijonov/git-darslik/issues)
yoki [bog'laning](https://solijonov.uz/contact/).
