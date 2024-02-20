/*let db;
fetch('stats.db')
  .then(response => response.arrayBuffer())
  .then(buffer => {
    db = new SQL.Database(new Uint8Array(buffer));
    const data = db.exec('SELECT * FROM Registry');
    console.log('Data:', data);
  })
  .catch(error => {
    console.error('Error opening database:', error);
  });
*/