

//pop ups
document.querySelectorAll('.popup').forEach(popup => {
    const parent = popup.parentNode
    popup.style.display = 'none';


  parent.addEventListener('mouseover', function () {
    popup.style.display = 'block';

  });
    parent.addEventListener('mouseout', function () {   
    popup.style.display = 'none';
});
});

//dragabble window
const box = document.getElementById("center");
const headd = document.querySelector("#center header");

let isDragging = false;
let offsetX = 0;
let offsetY = 0;

headd.addEventListener("mousedown", (e) => {
  e.preventDefault(); // prevent text selection

  isDragging = true;
  headd.style.cursor = "grabbing";

  const rect = box.getBoundingClientRect();
  offsetX = e.clientX - rect.left;
  offsetY = e.clientY - rect.top;
});

document.addEventListener("mousemove", (e) => {
  if (!isDragging) return;

  box.style.left = `${e.clientX - offsetX}px`;
  box.style.top = `${e.clientY - offsetY}px`;
});

document.addEventListener("mouseup", () => {
  if (!isDragging) return;

  isDragging = false;
  headd.style.cursor = "grab";
});

document.getElementById("close").onclick = function() {
    document.getElementById("center").style.display = "none";
        document.getElementById("book").style.display = "block";

}

document.getElementById("book").onclick = function() {
    document.getElementById("center").style.display = "block";
    document.getElementById("book").style.display = "none";



}