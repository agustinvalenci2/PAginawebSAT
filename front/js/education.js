var addEducationButton = document.getElementById("add-button");
var removeEducationButton = document.getElementById("remove-button");

function createInputBoxText(spanText, placeholder){
    //Elements
    const container = document.createDocumentFragment();
    const divElement = document.createElement("div");
    const spanElement = document.createElement("span");
    const inputElement = document.createElement("input");

    //set Attributes
    divElement.className = "input-box";
    spanElement.className = "details";
    spanElement.innerHTML = spanText;
    inputElement.type = "text";
    inputElement.placeholder = placeholder;
    
    //Add elements
    divElement.appendChild(spanElement);
    divElement.appendChild(inputElement);
    container.appendChild(divElement);
    return container;
}

function createInputBoxDate(spanText){
    //Elements
    const container = document.createDocumentFragment();
    const divElement = document.createElement("div");
    const spanElement = document.createElement("span");
    const inputElement = document.createElement("input");

    //set Attributes
    divElement.className = "input-box";
    spanElement.className = "details";
    spanElement.innerHTML = spanText;
    inputElement.type = "date";

    //Add elements
    divElement.appendChild(spanElement);
    divElement.appendChild(inputElement);
    container.appendChild(divElement);
    return container;
}

addEducationButton.onclick = function(){
    const education = document.getElementsByClassName("education")[0];
    const newEducationInfo = document.createDocumentFragment();
    const divElement = document.createElement("div");
    const hr = document.createElement("hr");
    const title = createInputBoxText("Title","Enter Title");
    const institution = createInputBoxText("Educational Institution","Enter Educational Institution");
    const startDate = createInputBoxDate("Start date");
    const endDate = createInputBoxDate("End date/Estimated end date");
    const country = createInputBoxText("Country","Enter country");
    const state = createInputBoxText("State","Enter state");
    const city = createInputBoxText("City","Enter city");
    
    //set Attributes
    divElement.className = "education-info";

    //Append elements
    divElement.appendChild(hr);
    divElement.appendChild(title);
    divElement.appendChild(institution);
    divElement.appendChild(startDate);
    divElement.appendChild(endDate);
    divElement.appendChild(country);
    divElement.appendChild(state);
    divElement.appendChild(city);

    newEducationInfo.appendChild(divElement);
    education.appendChild(newEducationInfo);
}

removeEducationButton.onclick = function(){
    const education = document.getElementsByClassName("education")[0];
    if(education.childElementCount>1) education.removeChild(education.lastChild);
}