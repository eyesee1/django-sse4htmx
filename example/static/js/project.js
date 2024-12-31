window.addEventListener('DOMContentLoaded', () => {
  document.addEventListener('htmx:afterRequest', afterSubmit);
  setupLogging();
});

function afterSubmit(evt) {
  if (evt.target.tagName.toLowerCase() != 'form') {
    return;
  }
  const target = evt.detail.target.nextElementSibling;
  let val = parseInt(target.textContent);
  val += 1;
  target.textContent = val.toString();
}

function setupLogging() {
  document.addEventListener('htmx:sseError', (evt) => {
    console.debug('Error opening SSE connection.', evt.detail);
  });
  document.addEventListener('htmx:sseOpen', (evt) => {
    console.debug('SSE connection opened:', evt.detail.source.url);
  });
  document.addEventListener('htmx:sseBeforeMessage', (evt) => {
    console.debug(
      'SSE Message received. Type:',
      evt.detail.type,
      'Detail:',
      evt.detail,
    );
  });
}
