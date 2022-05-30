var addLanguageButton = document.getElementById("add-button");
var removeLanguageButton = document.getElementById("remove-button");
var languageCounter = 1;


addLanguageButton.onclick = function(){
    let language = document.getElementsByClassName("language")[0];

    const scale = ["Basic","Intermediate","Advanced"];
    const newLanguageInfo = document.createDocumentFragment();

    //Elements
    const languageDiv = document.createElement("div");
    const inputBoxLanguageDiv = document.createElement("div");
    const languageSpan = document.createElement("span");
    const languageInput = document.createElement("input");

    const inputBoxLevelDiv = document.createElement("div");
    const levelLabel = document.createElement("label");
    const levelSelect = document.createElement("select");

    //Set attributes
    languageDiv.className = "language-info";
    inputBoxLanguageDiv.className = "input-box";
    languageSpan.className = "details";
    languageSpan.innerHTML = "Language";
    languageInput.type = "text";
    languageInput.placeholder = "Enter Language";
    inputBoxLevelDiv.className = "input-box";
    levelLabel.innerHTML = "Level";
    levelLabel.setAttribute("for","language_level");
    levelLabel.className = "details";
    levelSelect.name = "language_level";
    levelSelect.id = `language_level${languageCounter}`;
    languageCounter++;

    for (i in scale) {
        const optionElement = document.createElement("option");
        optionElement.value = parseInt(i)+1;
        optionElement.innerHTML = scale[i];
        levelSelect.appendChild(optionElement);
    }

    //Add elements to document
    inputBoxLanguageDiv.appendChild(languageSpan);
    inputBoxLanguageDiv.appendChild(languageInput);
    inputBoxLevelDiv.appendChild(levelLabel);
    inputBoxLevelDiv.appendChild(levelSelect);
    languageDiv.appendChild(inputBoxLanguageDiv);
    languageDiv.appendChild(inputBoxLevelDiv);
    newLanguageInfo.appendChild(languageDiv);

    language.appendChild(newLanguageInfo);

}

removeLanguageButton.onclick = function(){
    let language = document.getElementsByClassName("language")[0];
    if(language.childElementCount>1) language.removeChild(language.lastChild);
    languageCounter --;
}