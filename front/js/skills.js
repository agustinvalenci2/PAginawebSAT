var addSkillButton = document.getElementById("add-button");
var removeSkillButton = document.getElementById("remove-button");
var skillsCounter = 1;

addSkillButton.onclick = function(){
    let skills = document.getElementsByClassName("skills")[0];

    const scale = ["Basic","Intermediate","Advanced"];
    const newSkillsInfo = document.createDocumentFragment();

    //Elements
    const skillsDiv = document.createElement("div");
    const inputBoxSkillsDiv = document.createElement("div");
    const skillSpan = document.createElement("span");
    const skillInput = document.createElement("input");

    const inputBoxLevelDiv = document.createElement("div");
    const levelLabel = document.createElement("label");
    const levelSelect = document.createElement("select");

    //Set attributes
    skillsDiv.className = "skills-info";
    inputBoxSkillsDiv.className = "input-box";
    skillSpan.className = "details";
    skillSpan.innerHTML = "Skill";
    skillInput.type = "text";
    skillInput.placeholder = "Enter Skill";
    inputBoxLevelDiv.className = "input-box";
    levelLabel.innerHTML = "Level";
    levelLabel.setAttribute("for","skill_level");
    levelLabel.className = "details";
    levelSelect.name = "skill_level";
    levelSelect.id = `skill_level${skillsCounter}`;
    skillsCounter++;
    for (i in scale) {
        const optionElement = document.createElement("option");
        optionElement.value = parseInt(i)+1;
        optionElement.innerHTML = scale[i];
        levelSelect.appendChild(optionElement);
    }

    //Add elements to document
    inputBoxSkillsDiv.appendChild(skillSpan);
    inputBoxSkillsDiv.appendChild(skillInput);
    inputBoxLevelDiv.appendChild(levelLabel);
    inputBoxLevelDiv.appendChild(levelSelect);
    skillsDiv.appendChild(inputBoxSkillsDiv);
    skillsDiv.appendChild(inputBoxLevelDiv);
    newSkillsInfo.appendChild(skillsDiv);

    skills.appendChild(newSkillsInfo);

}

removeSkillButton.onclick = function(){
    let skills = document.getElementsByClassName("skills")[0];
    if(skills.childElementCount>1) skills.removeChild(skills.lastChild);
    skillsCounter --;
}