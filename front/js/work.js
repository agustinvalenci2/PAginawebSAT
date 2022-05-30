var addWorkButton = document.getElementById("add-button");
var removeWorkButton = document.getElementById("remove-button");
var workCounter = 1;

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

function createDescription(){
    const container = document.createDocumentFragment();
    const divDescription = document.createElement("div");
    const divInputBox = document.createElement("div");
    const labelElement = document.createElement("label");
    const textArea = document.createElement("textarea");

    //set attributes
    divDescription.className = "description";
    divInputBox.className = "input-box";
    labelElement.setAttribute("for","description");
    labelElement.innerHTML = "Description";
    textArea.name = "description";
    textArea.id = `description${workCounter}`;
    textArea.cols = "100";
    textArea.rows = "5";
    textArea.placeholder ="What did you do during the time you worked here?";
    workCounter++;

    //append childs
    divInputBox.appendChild(labelElement);
    divInputBox.appendChild(textArea);
    divDescription.appendChild(divInputBox);
    container.appendChild(divDescription);
    return container;
}

addWorkButton.onclick = function(){
    const work = document.getElementsByClassName("work")[0];
    const newWorkInfo = document.createDocumentFragment();
    const divElement = document.createElement("div");
    const hr = document.createElement("hr");
    const role = createInputBoxText("Role","Enter Role");
    const company = createInputBoxText("Company","Enter Company");
    const startDate = createInputBoxDate("Start date");
    const endDate = createInputBoxDate("End date/Estimated end date");
    const description = createDescription();

    //set Attributes
    divElement.className = "work-info";
    
    //Append elements
    divElement.appendChild(hr);
    divElement.appendChild(role);
    divElement.appendChild(company);
    divElement.appendChild(startDate);
    divElement.appendChild(endDate);

    newWorkInfo.appendChild(divElement);
    work.appendChild(newWorkInfo);
    work.appendChild(description);
}

removeWorkButton.onclick = function(){
    const work = document.getElementsByClassName("work")[0];
    if(work.childElementCount>2) {
        work.removeChild(work.lastChild);
        work.removeChild(work.lastChild);
    }
    workCounter -= 2;
}