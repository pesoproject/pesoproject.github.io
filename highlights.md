---
layout: page
title: Project Highlights
title_html: PESO Project <span class="accent">Highlights</span>
description: Short, plain-language looks at specific pieces of PESO's work, drawn from talks and posters.
section_tag: Impact
permalink: /highlights
---

Each highlight below started as a single slide with speaker notes prepared for a talk or poster session. The caption is a short summary in plain language; click a slide to see it full size.

<div class="highlight-grid" style="margin-top:8px;">
{% for h in site.data.highlights %}
<button type="button" class="highlight-card" data-title="{{ h.title | escape }}" data-caption="{{ h.caption | escape }}" data-pdf="{{ h.pdf }}">
  <div class="highlight-thumb"><img src="{{ h.thumbnail }}" alt="Slide: {{ h.title | escape }}" loading="lazy"></div>
  <div class="highlight-body">
    <h3>{{ h.title }}</h3>
    <p>{{ h.caption }}</p>
  </div>
</button>
{% endfor %}
</div>

<div class="highlight-modal" id="highlightModal" role="dialog" aria-modal="true" aria-labelledby="highlightModalTitle">
  <div class="highlight-modal-panel">
    <div class="highlight-modal-head">
      <h3 id="highlightModalTitle"></h3>
      <button type="button" class="highlight-modal-close" id="highlightModalClose" aria-label="Close">&times;</button>
    </div>
    <div class="highlight-modal-body">
      <iframe class="highlight-modal-pdf" id="highlightModalPdf" title="Full-size slide PDF"></iframe>
      <div class="highlight-modal-caption">
        <p id="highlightModalCaption"></p>
        <a class="pdf-fallback" id="highlightModalFallback" href="#" target="_blank" rel="noopener">Open PDF in a new tab</a>
      </div>
    </div>
  </div>
</div>

<script>
(function(){
  var modal = document.getElementById('highlightModal');
  var titleEl = document.getElementById('highlightModalTitle');
  var captionEl = document.getElementById('highlightModalCaption');
  var pdfEl = document.getElementById('highlightModalPdf');
  var fallbackEl = document.getElementById('highlightModalFallback');
  var closeBtn = document.getElementById('highlightModalClose');
  var lastFocused = null;

  function openModal(card){
    titleEl.textContent = card.getAttribute('data-title');
    captionEl.textContent = card.getAttribute('data-caption');
    var pdf = card.getAttribute('data-pdf');
    pdfEl.src = pdf;
    fallbackEl.href = pdf;
    lastFocused = document.activeElement;
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    closeBtn.focus();
  }

  function closeModal(){
    modal.classList.remove('open');
    document.body.style.overflow = '';
    pdfEl.src = '';
    if (lastFocused) lastFocused.focus();
  }

  document.querySelectorAll('.highlight-card').forEach(function(card){
    card.addEventListener('click', function(){ openModal(card); });
  });

  closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', function(e){
    if (e.target === modal) closeModal();
  });
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && modal.classList.contains('open')) closeModal();
  });
})();
</script>
