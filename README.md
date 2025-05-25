# Flask-Study – Anonymous Community MVP & Personal Flask Learning Journey

> ** Status: Development paused (May 2025)**  
> This project documents my structured journey of mastering Flask, starting from fundamentals to building an anonymous student community app.  
> As of now, I’m shifting my primary focus to intensive German language study (Goethe C1 level), while continuing Flask via weekly book-based sessions.

---

##  Project Goals

- Build core backend skills using Flask from the ground up
- Learn how to create secure, modular, and scalable web applications
- Ultimately design a **privacy-focused, anonymous community platform** for university students

---

##  Current Progress (as of May 2025)

| Component                          | Status        | Notes |
|-----------------------------------|---------------|-------|
| Basic Flask app structure         | ✅ Completed  | Routes, templates, CSS |
| User registration & login         | ✅ Working    | Flask-Login integration |
| Session & Flash message flow      | ✅ Working    | `@login_required`, navbar control |
| SQLAlchemy model setup            | ✅ Implemented | `User` model defined |
| `site.db` creation                | ✅ Verified   | `dict_keys(['user'])` confirmed |
| DB visibility in Codesandbox      | ⚠️ Blocked    | File not shown in UI due to sandboxing |
| Modularization (`extensions.py`)  | ✅ Completed  | db & login_manager split |

---

##  Status & Learning Shift

During the development of this MVP, I encountered limitations using GPT and web-based IDEs alone:

- Difficulty debugging internal Flask behavior in non-local environments
- File visibility and access issues in Codesandbox
- Lack of conceptual grounding despite working output

###  New Approach (May 2025 onward)

| Strategy             | Description |
|---------------------|-------------|
| 📘 Weekly Flask Study | Rebuilding knowledge via *Flask Web Development* (Miguel Grinberg) |
| 🇩🇪 Daily Focus        | Intensive German study for Goethe C1 (grammar, sentence transformation, fluency) |
| ⏸️ MVP Freeze         | MVP paused to prioritize deep learning and linguistic foundation |

---

##  Learning Journey (Initial Phase)

###  Completed Milestones

- Basic Flask setup & routing (`/`, `/about`, `/contact`)
- HTML form handling with GET/POST
- Inline and linked CSS styling
- Using `render_template()` with separated HTML files
- GitHub version control
- Created modular folders:

/Form input handling practice/
/Flask-Practice-(HTML in here)/
/Flask-Practice-(connected HTML)/

---

##  Future Plans

| Roadmap Item | Status |
|--------------|--------|
| Handling GET/POST separately | 🔜 Pending |
| Passing variables into templates | 🔜 Planned |
| Creating reusable templates with Jinja2 | 🔜 Planned |
| Deploying Flask apps to production | 🔜 Long-term |

---

##  Final Thought

> "This is not a failure, it’s calibration."  
> I’ll continue sharpening my backend skills weekly,  
> while investing my full capacity into language mastery and academic preparation.

This decision to pause the MVP and return to book-based learning is not a retreat, but a deliberate strategy aligned with my philosophy.  
Rather than rushing to complete a working product, I choose to internalize core principles, understand the architecture deeply, and build a foundation that can scale.  
My goal is not just to finish a project, but to become a developer who understands how to think structurally, debug independently, and design sustainably.  
This stage is a necessary recalibration to ensure that what I build in the future is both functional and principled.

---

##  Tech Stack

- Python 3.10+
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLite
- HTML & CSS
- Codesandbox / GitHub
