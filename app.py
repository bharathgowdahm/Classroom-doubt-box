import streamlit as st

st.set_page_config(page_title="Silent Classroom Doubt Box", page_icon="📦", layout="wide")

# --- Styles ---
st.markdown("""
<style>
.main {background:#05070f;}
h1 {background:linear-gradient(110deg,#a5b4fc,#e879f9,#67e8f9);-webkit-background-clip:text;color:transparent;}
.card {background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:16px;padding:18px;margin:10px 0;}
</style>
""", unsafe_allow_html=True)

st.title("Silent Classroom Doubt Box")
st.subheader("Ask fearlessly. Learn endlessly. — ಸಂದೇಹವಿಲ್ಲದೆ ಕೇಳಿ")

# session state
if "doubts" not in st.session_state:
    st.session_state.doubts = [
        {"subject":"DSA","q":"Stack vs Queue difference?","by":"Anonymous","status":"Answered"},
        {"subject":"OOP","q":"Explain polymorphism with example","by":"Anonymous","status":"Answered"},
        {"subject":"DBMS","q":"Why normalization needed?","by":"Anonymous","status":"Open"},
    ]

KB = {
 "recursion":"Recursion = function calls itself. Need base case + recursive case. Ex: factorial(n)=n*factorial(n-1).",
 "stack":"Stack=LIFO (push/pop). Queue=FIFO (enqueue/dequeue).",
 "queue":"Stack=LIFO (push/pop). Queue=FIFO (enqueue/dequeue).",
 "polymorphism":"Polymorphism = same method, different behavior. Ex: Shape.draw() -> Circle draws circle.",
 "normalization":"1NF atomic, 2NF no partial dependency, 3NF no transitive dependency.",
 "deadlock":"Deadlock = wait forever. Needs: mutual exclusion, hold-and-wait, no preemption, circular wait.",
 "flexbox":"Flexbox=1D layout. Grid=2D layout.",
 "pointer":"Pointer stores memory address. int *p = &x;",
 "git":"git add -> git commit -m -> git push. Branches for safe experiments.",
}

def ai_answer(q):
    ql=q.lower()
    for k,v in KB.items():
        if k in ql: return v
    return "Great question! Break it into small parts, check GeeksforGeeks/MDN, or join a live session."

tab1, tab2, tab3, tab4 = st.tabs(["📦 Doubt Box","🤖 AI Search","🔴 Live Sessions","🔗 Resources"])

with tab1:
    st.header("Drop a Doubt (Anonymous)")
    with st.form("doubt_form"):
        subject = st.selectbox("Subject",["DSA","OOP","DBMS","OS","Python","Java","Web Dev","Other"])
        question = st.text_area("Your doubt", placeholder="e.g. What is deadlock?")
        anon = st.checkbox("Stay anonymous", value=True)
        name = st.text_input("Display name (if not anonymous)")
        submitted = st.form_submit_button("Submit Doubt")
        if submitted:
            if len(question.strip())<10:
                st.error("Please describe in at least 10 characters.")
            else:
                by = "Anonymous" if anon else (name.strip() or "Learner")
                st.session_state.doubts.insert(0, {"subject":subject,"q":question,"by":by,"status":"Open"})
                st.success("Doubt submitted! AI Hint: "+ai_answer(question))

    st.header("Community Doubts")
    for d in st.session_state.doubts:
        st.markdown(f"""<div class="card"><b>[{d['subject']}]</b> {d['q']}<br>
        <small>by {d['by']} | {d['status']} | 🤖 Hint: {ai_answer(d['q'])}</small></div>""", unsafe_allow_html=True)

with tab2:
    st.header("AI Search")
    q = st.text_input("Ask anything", placeholder="Try: what is a deadlock?")
    if st.button("Ask AI"):
        st.info("🤖 "+ai_answer(q))

with tab3:
    st.header("Live Sessions")
    st.markdown("""<div class="card">🔴 <b>LIVE NOW:</b> DSA Doubt Marathon — Recursion & Trees<br>
    <a href="#">Join Live</a></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="card">📅 <b>Today 6 PM:</b> Python for Beginners Q&A</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="card">📅 <b>Tomorrow 11 AM:</b> DBMS & SQL Interview Prep</div>""", unsafe_allow_html=True)

with tab4:
    st.header("Direct Learning Links")
    st.markdown("""
- [GeeksforGeeks](https://www.geeksforgeeks.org)
- [MDN Web Docs](https://developer.mozilla.org)
- [Stack Overflow](https://stackoverflow.com)
- [NPTEL](https://nptel.ac.in)
- [Khan Academy](https://www.khanacademy.org)
""")
    st.header("Live Updates")
    st.write("• Anonymous learner asked about BST")
    st.write("• SQL Joins doubt resolved by mentor")
    st.write("• 23 new learners joined this hour")

st.sidebar.info("Built by Bharath Gowda | 2nd year CSE\nGitHub + LinkedIn portfolio project")
