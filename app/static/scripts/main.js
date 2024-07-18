function toggle_accordion(button) {
  /* Toggle between adding and removing the "active" class,
  to highlight the button that controls the panel */
  button.classList.toggle("active");

  /* Toggle between hiding and showing the active panel */
  var panel = button.nextElementSibling;
  if (panel.style.display === "block") {
    panel.style.display = "none";
  } else {
    panel.style.display = "flex";
  }
}

console.log("called");
const form = document.getElementById('form');
form.addEventListener('submit', function(e) {
  e.preventDefault();
  const payload = new FormData(form);
  console.log([...payload]);
  fetch('/api/timeline_post',{
    method: 'POST',
    body: payload,
  }).then(res => res.json()
    ).then(
    data => {
      console.log(data);
      if ('error' in data){
        const parent = document.getElementById("error");
        parent.innerHTML = '';
        const text = document.createTextNode(`Error: ${data.error}`);
        parent.appendChild(text);
      }else{
        const newDiv = document.createElement("div");
        const head = document.createTextNode(`${data.name}: ${data.created_at}`);
        const details = document.createTextNode(`${data.content}`);
        newDiv.appendChild(head);
        newDiv.appendChild(details);
        const parent = document.getElementById('submission-form');
        parent.appendChild(newDiv);
      }
      
    }
  )
})
