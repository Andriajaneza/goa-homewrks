const form = document.getElementById('formTag');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    let textValue = e.target.elements.text.value;

    console.log(textValue);

    const ul = document.createElement('ul');
    const li = document.createElement('li');
    const Deletebtn = document.createElement('button');
    const editBtn = document.createElement('button');
    Deletebtn.textContent = 'Delete';

    ul.appendChild(li);
    ul.appendChild(Deletebtn);
    ul.appendChild(editBtn);

    li.textContent = textValue;
    editBtn.textContent = 'Edit The Task';

    Deletebtn.addEventListener('click', () => {
        ul.removeChild(li);
        ul.removeChild(Deletebtn);
        ul.removeChild(editBtn);
    });

    editBtn.addEventListener('click', () => {
        const edited = prompt('Please enter a text and edit the task');
        li.textContent = edited;
    })

    document.body.appendChild(ul);
});