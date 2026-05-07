function addData() {

  const name = document.getElementById("name").value;
  const feedback = document.getElementById("feedback").value;

  fetch(`http://127.0.0.1:8000/add?name=${name}&feedback=${feedback}`, {
    method: "POST"
  })
  .then(res => res.json())
  .then(() => {
      loadData();
  });

}

function loadData() {

  fetch("http://127.0.0.1:8000/feedback")

    .then(res => res.json())

    .then(res => {

      const table = document.getElementById("table");

      table.innerHTML = `
      <tr>
        <th>Name</th>
        <th>Feedback</th>
      </tr>
      `;

      res.data.forEach(row => {

        table.innerHTML += `
        <tr>
          <td>${row[1]}</td>
          <td>${row[2]}</td>
        </tr>
        `;

      });

    });

}

loadData();