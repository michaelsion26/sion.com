document.getElementById("openQuiz").onclick = () => {
    document.getElementById("quizModal").style.display = "block";
};

document.querySelector(".close").onclick = () => {
    document.getElementById("quizModal").style.display = "none";
};

document.getElementById("startQuiz").onclick = () => {
    const nombre = document.getElementById('nombre').value;
    const cantidad = document.getElementById('cantidad').value;
    const tiempo = document.getElementById('tiempo').value;

    fetch('/get_quiz', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({cantidad})
    })
    .then(res=>res.json())
    .then(data=>{
        localStorage.setItem('quiz', JSON.stringify(data));
        localStorage.setItem('nombre', nombre);
        localStorage.setItem('tiempo', tiempo);
        window.location.href = '/quiz';
    });
};
