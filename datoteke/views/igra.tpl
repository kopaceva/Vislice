% import model
<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>

  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
    <small>Študentje</small>
  </blockquote>

  <h2>{{igra.pravilni_del_gesla()}}</h2>

  Nepravilne črke : {{igra.nepravilni_ugibi()}} 

  % preostali_poskusi = model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1
  <br>Število preostalih poskusov: {{preostali_poskusi}}
  <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">

% if poskus == model.ZMAGA:
<h2>ZMAGA!</h2>

% elif poskus == model.PORAZ:

<h2>Poraz!</h2>
Pravilno geslo je {{igra.geslo}}.

<form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
</form>

% else:
<form action="/igra/{{id_igre}}/" method="post">
    črka: <input type="text" name = "crka">
    <button type="submit">Pošlji ugib</button>
</form>
% end

</body>
</html>