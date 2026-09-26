import streamlit as st
import random
import time

st.set_page_config(page_title="Python Quiz Game")

questions = {
    "Easy": [
        ("what is 12 + 15","27"),
        ("what is 144 / 12","12"),
        ("what is square root of 81","9"),
        ("what is 7 * 8","56"),
        ("what is 100 - 45","55"),
        ("value of pi (approx)","3.14"),
        ("what is 2 power 5","32"),
        ("what is LCM of 4 and 6","12"),
        ("what is HCF of 8 and 12","4"),
        ("area of square with side 4","16"),
        ("unit of force","newton"),
        ("unit of current","ampere"),
        ("speed = distance / ?","time"),
        ("chemical symbol of oxygen","o"),
        ("pH value of neutral solution","7"),
        ("planet known as red planet","mars"),
        ("largest planet in solar system","jupiter"),
        ("sun is a","star"),
        ("process of water cycle evaporation + condensation + ?","precipitation"),
        ("gas used by plants in photosynthesis","carbon dioxide"),
        ("full form of CPU","central processing unit"),
        ("full form of RAM","random access memory"),
        ("which is brain of computer","cpu"),
        ("which language is used for web structure","html"),
        ("which language is used for styling","css"),
        ("python is interpreted or compiled","interpreted"),
        ("keyword to define function in python","def"),
        ("what is output of 5 % 2","1"),
        ("what is output of 10 // 3","3"),
        ("list is mutable or immutable","mutable"),
        ("tuple is mutable or immutable","immutable"),
        ("index starts from in python","0"),
        ("loop for fixed iteration","for"),
        ("loop for condition based","while"),
        ("boolean values","true false"),
        ("who invented computer","charles babbage"),
        ("father of c language","dennis ritchie"),
        ("national animal of india","tiger"),
        ("national bird of india","peacock"),
        ("capital of india","delhi"),
        ("who wrote national anthem of india","rabindranath tagore"),
        ("independence year of india","1947"),
        ("largest ocean","pacific"),
        ("smallest prime number","2"),
        ("next prime after 7","11"),
        ("what is 15 percent of 100","15"),
        ("simple interest formula symbol","p r t"),
        ("area of rectangle formula","l b"),
        ("perimeter of square formula","4 a"),
        ("what is 3/4 as decimal","0.75")
    ],

    "Medium": [
        ("what is square root of 625","25"),
        ("what is 15 * 12","180"),
        ("what is value of 2^6","64"),
        ("what is 121 / 11","11"),
        ("what is 45 percent of 200","90"),
        ("what is formula of area of circle","pi r square"),
        ("what is value of pi upto 2 decimal","3.14"),
        ("what is LCM of 12 and 18","36"),
        ("what is HCF of 18 and 24","6"),
        ("what is next number in series 2 4 8 16 ?","32"),
        ("unit of power","watt"),
        ("unit of voltage","volt"),
        ("formula of force","mass acceleration"),
        ("speed of light in vacuum (approx km/s)","300000"),
        ("ohm law formula","v i r"),
        ("chemical symbol of potassium","k"),
        ("chemical formula of carbon dioxide","co2"),
        ("atomic number of hydrogen","1"),
        ("gas used in respiration","oxygen"),
        ("acid in lemon","citric acid"),
        ("who discovered gravity","newton"),
        ("largest gland in human body","liver"),
        ("human heart has how many chambers","4"),
        ("which planet has rings","saturn"),
        ("nearest star to earth","sun"),
        ("full form of URL","uniform resource locator"),
        ("full form of IP","internet protocol"),
        ("which device stores data permanently","hard disk"),
        ("which language is used for backend","python"),
        ("which symbol is used for comments in python","#"),
        ("output of 2 + 3 * 4","14"),
        ("output of 10 % 4","2"),
        ("output of 5 // 2","2"),
        ("what is data type of 5.5","float"),
        ("what is data type of true","boolean"),
        ("who is father of java","james gosling"),
        ("who is father of python","guido van rossum"),
        ("national sport of india (officially none)","none"),
        ("largest continent","asia"),
        ("longest river in world","nile"),
        ("value of sin 90 degree","1"),
        ("value of cos 0 degree","1"),
        ("value of tan 45 degree","1"),
        ("what is 0 factorial","1"),
        ("what is log10 100","2"),
        ("what is derivative of x^2","2x"),
        ("what is integration of 1 dx","x"),
        ("what is binary of 10","1010"),
        ("decimal of 101","5"),
        ("what is 1 byte in bits","8")
    ],

    "Hard": [
        ("what is derivative of sin x","cos x"),
        ("what is derivative of ln x","1/x"),
        ("integration of x dx","x square by 2"),
        ("value of limit x->0 (sin x)/x","1"),
        ("what is determinant of identity matrix","1"),
        ("what is eigenvalue of identity matrix","1"),
        ("what is rank of identity matrix 3x3","3"),
        ("what is formula of binomial theorem","ncr"),
        ("what is 5 factorial","120"),
        ("what is value of log e base e","1"),
        ("newton second law formula","f m a"),
        ("unit of electric field","newton per coulomb"),
        ("formula of kinetic energy","half m v square"),
        ("formula of potential energy","m g h"),
        ("what is escape velocity depends on","mass radius"),
        ("what is coulomb law formula","k q1 q2 r square"),
        ("what is ohm law formula","v i r"),
        ("what is power formula in electricity","v i"),
        ("unit of capacitance","farad"),
        ("unit of resistance","ohm"),
        ("hybridization in methane","sp3"),
        ("ph of strong acid approx","1"),
        ("ph of strong base approx","14"),
        ("avogadro number approx","6.022e23"),
        ("molar mass of h2o","18"),
        ("time complexity of binary search","log n"),
        ("time complexity of linear search","n"),
        ("time complexity of bubble sort worst","n square"),
        ("stack follows which principle","lifo"),
        ("queue follows which principle","fifo"),
        ("what is output of 2**3**2","512"),
        ("what is output of len([1,2,3,4])","4"),
        ("what is data type of {1,2,3}","set"),
        ("what is slicing [1,2,3,4][1:3]","2 3"),
        ("what is keyword to handle exception","try"),
        ("who developed relativity theory","einstein"),
        ("planck constant symbol","h"),
        ("speed of light in m/s","3e8"),
        ("which particle has no charge","neutron"),
        ("which particle is negative","electron"),
        ("sql command to retrieve data","select"),
        ("sql command to delete data","delete"),
        ("primary key is unique or not","unique"),
        ("foreign key used for","relation"),
        ("normalization used for","reduce redundancy"),
        ("what is 2 complement of 1","1"),
        ("what is 1s complement of 0","1"),
        ("what is ascii of A","65"),
        ("what is boolean algebra 1+1","1"),
        ("what is boolean algebra 1.0","0")
    ]
}

if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.finished = False
    st.session_state.questions = []
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.wrong = 0
    st.session_state.answers = []
    st.session_state.name = ""
    st.session_state.difficulty = "Easy"
    st.session_state.total = 5
    st.session_state.start_time = 0
    st.session_state.elapsed = 0

if not st.session_state.started and not st.session_state.finished:

    st.title("Python Quiz Game")

    st.write("Choose your difficulty level and test your knowledge.")

    name = st.text_input("Enter your name")

    difficulty = st.selectbox(
        "Choose difficulty level",
        ["Easy", "Medium", "Hard"]
    )

    total = st.number_input(
        "How many questions would you like to attempt? (1-50)",
        min_value=1,
        max_value=50,
        value=5,
        step=1
    )

    if st.button("Start Quiz"):

        if name.strip() == "":
            st.error("Please enter your name.")

        else:
            st.session_state.name = name
            st.session_state.difficulty = difficulty
            st.session_state.total = total

            st.session_state.questions = random.sample(
                questions[difficulty],
                k=total
            )

            st.session_state.current = 0
            st.session_state.score = 0
            st.session_state.wrong = 0
            st.session_state.answers = []

            st.session_state.start_time = time.perf_counter()

            st.session_state.started = True
            st.session_state.finished = False

            st.rerun()


elif st.session_state.started:

    q_no = st.session_state.current + 1

    question, correct_answer = st.session_state.questions[
        st.session_state.current
    ]

    st.write(
        "Question",
        q_no,
        "of",
        st.session_state.total
    )

    st.write(question)

    answer = st.text_input(
        "Enter the answer",
        key=f"answer_{st.session_state.current}"
    )

    if st.button("Next"):

        if answer.strip() == "":
            st.error("Please enter an answer.")

        else:

            is_correct = (
                answer.strip().lower()
                == correct_answer.lower()
            )

            if is_correct:
                st.session_state.score += 1
            else:
                st.session_state.wrong += 1

            st.session_state.answers.append({
                "question": question,
                "user_answer": answer,
                "correct_answer": correct_answer,
                "correct": is_correct
            })

            if (
                st.session_state.current + 1
                < st.session_state.total
            ):

                st.session_state.current += 1
                st.rerun()

            else:

                st.session_state.elapsed = (
                    time.perf_counter()
                    - st.session_state.start_time
                )

                st.session_state.started = False
                st.session_state.finished = True

                st.rerun()


elif st.session_state.finished:

    score = st.session_state.score
    wrong = st.session_state.wrong
    total = st.session_state.total

    percentage = (score * 100) / total

    st.write("Quiz Completed!")

    st.write("Name:", st.session_state.name)

    st.write(
        "Difficulty:",
        st.session_state.difficulty
    )

    st.write("Total Questions:", total)

    st.write("Correct:", score)

    st.write("Wrong:", wrong)

    st.write(
        "Percentage:",
        f"{percentage:.2f}%"
    )

    st.write(
        "Total time:",
        f"{st.session_state.elapsed:.2f} seconds"
    )

    st.write("Answer Review:")

    for i, item in enumerate(
        st.session_state.answers,
        1
    ):

        st.write(
            i,
            item["question"]
        )

        st.write(
            "Your answer:",
            item["user_answer"]
        )

        if item["correct"]:

            st.write("Correct")

        else:

            st.write(
                "Correct answer:",
                item["correct_answer"]
            )

    st.write("Can you play game again?")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Yes"):

            st.session_state.started = False
            st.session_state.finished = False
            st.session_state.questions = []
            st.session_state.current = 0
            st.session_state.score = 0
            st.session_state.wrong = 0
            st.session_state.answers = []

            st.rerun()

    with col2:

        if st.button("No"):

            st.write(
                f"Thanks for playing, "
                f"{st.session_state.name} / Quiz Ended"
            )