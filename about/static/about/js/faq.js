function faqDropdownOnClick(id) {
  document.getElementById(id).classList.toggle("show");
}

window.onclick = function (event) {
  var dropdownElements = document.getElementsByClassName("faq__dropdown");

  if (dropdownElements.length) {
    var j;

    for (j = 0; j < dropdownElements.length; j++) {
      var btnName = "faqDropdownBtn-" + j;
      var btnElement = document.getElementById(btnName);

      if (!event.target.matches("#" + btnName)) {
        if (btnElement.classList.contains("show")) {
          btnElement.classList.remove("show");
        }
      }
    }
  }
};
