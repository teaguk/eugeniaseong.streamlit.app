import streamlit as st
import base64

st.title("eugenia site!!")
st.header("Climate Crash")

description = """
I made this game based on SDG 13. It's about a young animal  
trying to save its village from climate change! Help the animal  
and make it happy!!
"""
st.write(description)

# Base64 encode images
def get_base64_image(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

image1_base64 = get_base64_image("1.png")
image2_base64 = get_base64_image("2.png")
image3_base64 = get_base64_image("3.png")
image4_base64 = get_base64_image("4.png")
image5_base64 = get_base64_image("5.png")
chicken_base64 = get_base64_image("chicken.png")

html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {{ position: relative; display: inline-block; outline: none; }}
    .clickable-area {{ position: absolute; width: 60px; height: 65px; cursor: pointer; border: 2px solid red; }}
    .multi-box {{ display: none; }}
    .fade-text {{ opacity: 0; transition: opacity 2s ease-in-out; font-size: 20px; font-weight: bold; color: white; text-shadow: 2px 2px 4px black; position: absolute; top: 20px; left: 50%; transform: translateX(-50%); text-align: center; width: 100%; }}
    .visible {{ opacity: 1; }}
    .blackout {{ position: absolute; top: 0; left: 0; width: 600px; height: 100%; background-color: black; z-index: 10; display: none; }}
    .chicken {{ position: absolute; bottom: 20px; left: 220px; width: 100px; display: none; z-index: 5; }}
    .speech {{ position: absolute; top: 20px; left: 50%; transform: translateX(-50%); font-size: 20px; color: yellow; font-weight: bold; background-color: rgba(0, 0, 0, 0.6); padding: 10px 20px; border-radius: 10px; display: none; z-index: 11; }}
    .health-bar-container {{ position: absolute; top: 10px; left: 50%; transform: translateX(-50%); width: 500px; height: 14px; background-color: #444; border: 2px solid #fff; display: none; z-index: 20; }}
    .health-bar {{ height: 100%; background-color: #4caf50; width: 100%; }}
    .quiz-box {{ position: absolute; top: 35px; left: 50%; transform: translateX(-50%); background: white; padding: 12px; border: 2px solid green; border-radius: 10px; display: none; z-index: 30; width: 480px; }}
    .option-button {{ display: block; margin: 8px auto; padding: 10px 20px; font-size: 15px; background-color: #e0e0e0; border: none; border-radius: 5px; cursor: pointer; }}
    .option-button:hover {{ background-color: #d0ffd0; }}
  </style>
</head>
<body>
  <div class="container" tabindex="0" onkeydown="moveChicken(event)">
    <img id="main-image" src="data:image/png;base64,{image1_base64}" width="600">

    <div id="box1" class="clickable-area" style="top: 80px; left: 270px;" onclick="changeImage()"></div>
    <div id="box2" class="clickable-area multi-box" style="top: 120px; left: 65px;" onclick="boxClicked(1)"></div>
    <div id="box3" class="clickable-area multi-box" style="top: 120px; left: 210px;" onclick="boxClicked(2)"></div>
    <div id="box4" class="clickable-area multi-box" style="top: 125px; left: 370px;" onclick="boxClicked(3)"></div>
    <div id="box5" class="clickable-area multi-box" style="top: 230px; left: 150px;" onclick="boxClicked(4)"></div>
    <div id="box6" class="clickable-area multi-box" style="top: 120px; left: 515px;" onclick="boxClicked(5)"></div>
    <div id="box7" class="clickable-area multi-box" style="top: 220px; left: 455px;" onclick="boxClicked(6)"></div>

    <div id="fade-text" class="fade-text">It was a peaceful day until the Evil Dude came by...</div>
    <div id="blackout" class="blackout"></div>
    <img id="chicken" class="chicken" src="data:image/png;base64,{chicken_base64}" />
    <div id="chicken-speech" class="speech">I have to do something!</div>

    <div id="health-bar-container" class="health-bar-container">
      <div id="health-bar" class="health-bar"></div>
    </div>

    <div id="quiz-box" class="quiz-box">
      <div id="question-text"></div>
      <button class="option-button" onclick="submitAnswer(0)"></button>
      <button class="option-button" onclick="submitAnswer(1)"></button>
      <button class="option-button" onclick="submitAnswer(2)"></button>
      <div id="result-text"></div>
    </div>
  </div>

  <script>
    let currentImage = "1";
    let chickenLeft = 220;
    let movementAllowed = false;
    const questions = [
      {{ text: "What is the main cause of climate change?", options: ["Volcanoes", "Solar flares", "Human activities"], correct: 2 }},
      {{ text: "Which gas is most responsible for global warming?", options: ["Oxygen", "Carbon dioxide", "Nitrogen"], correct: 1 }},
      {{ text: "What can we do to reduce climate change?", options: ["Burn more coal", "Use renewable energy", "Use more plastic"], correct: 1 }}
    ].map(q => ({{ ...q }})); // Ensures clean JS objects

    let currentQuestion = 0;

    function changeImage() {{
      document.getElementById("main-image").src = "data:image/png;base64," + "{image2_base64}";
      document.getElementById("box1").style.display = "none";
      const boxes = document.getElementsByClassName("multi-box");
      for (let i = 0; i < boxes.length; i++) boxes[i].style.display = "block";
      currentImage = "2";
    }}

    function boxClicked(boxNumber) {{
      if (currentImage === "2" && boxNumber === 1) {{
        document.getElementById("main-image").src = "data:image/png;base64," + "{image3_base64}";
        document.querySelectorAll(".multi-box").forEach(box => box.style.display = "none");
        document.getElementById("fade-text").classList.add("visible");
        currentImage = "3";

        setTimeout(() => {{
          document.getElementById("fade-text").style.display = "none";
          document.getElementById("blackout").style.display = "block";

          setTimeout(() => {{
            document.getElementById("blackout").style.display = "none";
            document.getElementById("main-image").src = "data:image/png;base64," + "{image4_base64}";
            document.getElementById("chicken").style.display = "block";
            document.getElementById("chicken-speech").style.display = "block";
            document.querySelector(".container").focus();
            currentImage = "4";
            setTimeout(() => {{
              document.getElementById("chicken-speech").style.display = "none";
              movementAllowed = true;
            }}, 2000);
          }}, 3000);
        }}, 2500);
      }}
    }}

    function moveChicken(event) {{
      if (!movementAllowed) return;
      const chicken = document.getElementById("chicken");
      if (!chicken) return;

      if (event.key === "ArrowLeft") chickenLeft = Math.max(0, chickenLeft - 20);
      else if (event.key === "ArrowRight") chickenLeft = Math.min(500, chickenLeft + 20);
      chicken.style.left = chickenLeft + "px";

      if (chickenLeft + 100 >= 600 && currentImage === "4") {{
        currentImage = "5";
        chicken.style.display = "none";
        document.getElementById("main-image").src = "data:image/png;base64," + "{image5_base64}";
        document.getElementById("health-bar-container").style.display = "block";
        document.getElementById("quiz-box").style.display = "block";
        loadQuestion();
      }}
    }}

    function loadQuestion() {{
      const q = questions[currentQuestion];
      document.getElementById("question-text").innerText = q.text;
      document.querySelectorAll(".option-button").forEach((btn, i) => btn.innerText = q.options[i]);
      document.getElementById("result-text").innerText = "";
    }}

    function submitAnswer(choice) {{
      const correct = questions[currentQuestion].correct;
      const result = document.getElementById("result-text");
      if (choice === correct) {{
        result.innerText = "✅ Correct!";
        result.style.color = "green";
        setTimeout(() => {{
          currentQuestion++;
          if (currentQuestion < questions.length) loadQuestion();
          else document.getElementById("quiz-box").innerHTML = "<h3>🎉 Well done! You've finished the quiz!</h3>";
        }}, 1000);
      }} else {{
        result.innerText = "❌ Wrong answer. Try again!";
        result.style.color = "red";
      }}
    }}
  </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=1000)
