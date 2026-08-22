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

## Repo qanday tuzilgan

Ikki qismdan iborat:

* **`main`** — shu README, ya'ni yo'riqnoma.
* **`xarajat`** — loyihaning o'zi. Darslikda qilingan commitlar aynan shu
  branchda, boshqa hech narsa aralashmagan holda turibdi.

Ular ataylab ajratilgan: darslikda `git log` chiqishini ko'rsatganimda, siz shu
yerda **xuddi o'sha** ro'yxatni ko'rishingiz kerak — orasiga README commitlari
tushib qolmasin.

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
git log --oneline          # o'sha qismdagi commitlar
git switch xarajat         # loyihaning oxirgi holatiga qaytish
```

Taglar 2-qismdan boshlanadi: 1-qismda Git sozlangan, lekin hali loyiha
yo'q edi.

Branchlar ham ataylab o'chirilmagan. Darslikda branch ochib, merge qilib,
conflict yaratgan bo'lsak — o'sha branchlar shu yerda turibdi:

```bash
git branch -a              # barcha branchlar, remote'dagilari bilan
```

## Darsliklar

1. [Git nega kerak va uni qanday sozlaymiz?](https://solijonov.uz/writing/git-nega-kerak-va-sozlash/)
2. [git add nega kerak: fayl commitgacha uch bosqichdan o'tadi](https://solijonov.uz/writing/git-add-commit-uch-bosqich/) — tag: `qism-2`

Qolganlari chiqqan sari shu ro'yxatga qo'shiladi.

---

Savol yoki xato topsangiz — [Issue oching](https://github.com/AsadbekSolijonov/git-darslik/issues)
yoki [bog'laning](https://solijonov.uz/contact/).
