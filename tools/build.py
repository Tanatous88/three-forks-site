import sys, html

e = html.escape

UNITS = [
  dict(id='garage', group='farm', name='The Garage', kicker='Garage-themed studio on the farm',
       specs='Sleeps 4 · Studio · 2 queen beds · 1 bath', rating='5.0', reviews=110, badge='Top 1% of homes on Airbnb',
       price=141, link='https://airbnb.com/h/threeforksgarage',
       blurb='A stylish, one-of-a-kind studio on five acres, 50 feet outside Pullman city limits and 3 miles from WSU. Close to town, far enough to unwind.',
       perks=['Queen Sleep Number bed plus a queen Murphy bed',
              'Full kitchen and in-unit washer and dryer',
              'Foosball, classic arcade games, big-screen TV and an electric fireplace',
              'Private fenced backyard with covered patio, fire pit, grill and play set',
              'Level 2 EV charger at the unit',
              'A work desk built from a truck tailgate'],
       tags=['Pets welcome', 'EV charger', 'Full kitchen', 'Farm animals'],
       note=None,
       alts=['Living area with leather sofas under a corrugated metal ceiling', 'Queen bed beside a vintage red gas pump',
             'Open-plan living room and TV', 'Full kitchen with retro red refrigerator', 'Desk made from a red truck tailgate',
             'Classic arcade cabinet', 'Aerial view of The Garage among the pines']),
  dict(id='bunkhouse', group='farm', name='The Bunkhouse', kicker='Western-themed rustic retreat',
       specs='Sleeps 4 · 1 bedroom · Queen + sofa bed · 1 bath', rating='4.99', reviews=74, badge='Top 1% of homes on Airbnb',
       price=139, link='https://airbnb.com/h/threeforksbunkhouse',
       blurb='A warm, barn-style hideout where you can watch the Palouse hills glow gold at sunset and fall asleep to real quiet.',
       perks=['Queen Sleep Number bed, plus a pull-out couch in the living room',
              'Private fenced yard with a dedicated dog run and BBQ grill',
              'Level 2 EV charger in the covered carport',
              '50-inch TV, work desk and air conditioning',
              'Mini Highland cows, pigs and fainting goats a short stroll away'],
       tags=['Pets welcome', 'EV charger', 'Dog run', 'Farm animals'],
       note='Kitchenette only: fridge, microwave, toaster oven and Keurig. No stove or kitchen sink.',
       alts=['Bunkhouse living room with red accents', 'Bedroom with wagon-wheel wall decor', 'Living room with red accent wall',
             'Kitchenette and dining nook', 'Bathroom', 'Covered porch with red door', 'Fenced yard with wagon-wheel gate']),
  dict(id='studio', group='walnut', name='The Studio', kicker='Karaoke, arcade and a 100-inch screen',
       specs='Sleeps 6 · 2 bedrooms · 3 queen beds · 1.5 baths', rating='4.97', reviews=31, badge='Top 10% of homes on Airbnb',
       price=195, link='https://airbnb.com/h/threeforksstudio',
       blurb='A music-themed retreat with retro decor and mood lighting, built for groups who want their stay to be the fun part of the trip.',
       perks=['Karaoke room with a sound-dampened recording booth',
              'UHD projector with a 100-inch screen for movie nights',
              'Classic arcade machine, record player and board games',
              'Sleep Number bed, plus a Murphy bed under a glowing ON AIR sign',
              'Washer and dryer, dedicated workspace, on-site parking',
              'Walkable to downtown Pullman, easy for WSU and U of I events'],
       tags=['Pets welcome', 'Karaoke', 'Projector', 'Near downtown'],
       note='Kitchenette only (fridge, microwave, toaster, Keurig). Lower half of a duplex, so you may hear the neighbors upstairs.',
       alts=['Living room with green sectional', 'Karaoke recording booth with neon sign', 'Guitars on the wall beside the karaoke room',
             'Vintage-style record player', 'Bedroom with green pillows', 'Dining table and open living space', 'Snack bar and coffee station']),
  dict(id='nook', group='walnut', name='The Midnight Nook', kicker='Cozy one-bedroom suite for two',
       specs='Sleeps 2 · 1 bedroom · Queen bed · 1 bath', rating='4.92', reviews=13, badge='Guest favorite',
       price=125, link='https://airbnb.com/h/themidnightnook',
       blurb='An indigo-inspired suite where modern farmhouse charm meets total comfort. Crisp, clean and quiet.',
       perks=['Electric fireplace in a spacious lounge',
              'Full kitchen with stainless appliances',
              'Stocked coffee and snack station',
              'Spa-style bath with navy tile and fluffy towels',
              '4K smart TVs, fast Wi-Fi and laundry in the building',
              'Level 2 EV charger on site, about a 10-minute walk to Cougar Plaza'],
       tags=['EV charger', 'Full kitchen', 'Fireplace', 'Near downtown'],
       note='No pets in this unit.',
       alts=['Lounge with fireplace and TV', 'Queen bed with knit throw', 'Full kitchen', 'Electric fireplace', 'Coffee and snack station',
             'Bathroom with navy shower curtain', 'Grey reclining sofa']),
  dict(id='cosmo', group='walnut', name='The Cosmopolitan', kicker='Modern two-bedroom with a chef’s kitchen',
       specs='Sleeps 4 · 2 bedrooms · 2 queen beds · 1 bath', rating='5.0', reviews=19, badge='Top 5% of homes on Airbnb',
       price=132, link='https://airbnb.com/h/thecougarcosmo',
       blurb='High-end living with modern flair, two blocks from downtown shops and dining.',
       perks=['Chef’s kitchen with new stainless appliances, dishwasher and bar seating',
              '4K smart TVs in the living room and both bedrooms',
              'Open, airy living space with a fireplace',
              'Sleek black-and-white bath and premium linens',
              'Laundry, climate control and a Level 2 EV charger on site'],
       tags=['EV charger', 'Chef’s kitchen', 'Fireplace', 'Near downtown'],
       note='No pets in this unit.',
       alts=['Living room with sectional sofa', 'Chef’s kitchen with stainless appliances', 'Bedroom', 'Fireplace and wall-mounted TV',
             'Second bedroom', 'Bathroom', 'Living room, wide view']),
  dict(id='cottage', group='hill', name='The Cottage', kicker='Restored 1930s home on Pioneer Hill',
       specs='Sleeps 8 · 3 bedrooms · 2 queens + 1 king · 2 baths', rating='5.0', reviews=10, badge='Top 5% of homes on Airbnb',
       price=230, link='https://airbnb.com/h/thecougcottage',
       blurb='Historic charm meets contemporary comfort after a six-month, top-to-bottom renovation. Room for the whole family, a short walk from downtown and WSU.',
       perks=['Sleep Number beds and a TV in all three bedrooms',
              'Two living spaces: upstairs living room and a downstairs media lounge',
              'Bonus recreation area for games',
              'Full kitchen, washer and dryer',
              'Private backyard, front porch and gas grill',
              'Private parking, about a 5-minute walk to Cougar Plaza'],
       tags=['Pets welcome', 'Sleeps 8', 'Full kitchen', 'Walk to WSU'],
       note=None,
       alts=['The Cottage exterior with arched front door', 'Living room with large sectional', 'Living room with fireplace',
             'Bedroom', 'Second bedroom', 'Media lounge with TV', 'Bathroom with double vanity']),
]

GROUPS = [
  ('farm', 'The Farm', 'Five acres at the edge of town · 3 miles from WSU',
   'Two stays on our own farmstead, set in a wheat field with wide-open Palouse views. We live here too, along with the mini Highland cows, pigs and fainting goats.'),
  ('walnut', 'Walnut Street', 'Near downtown Pullman · about a mile from WSU',
   'Three stays on the same street, a three-minute walk apart and a short walk from downtown restaurants and shops.'),
  ('hill', 'Pioneer Hill', 'Quiet residential street · walk to downtown and WSU',
   'Our largest home, on one of Pullman’s historic hills.'),
]

def unit_html(u, flip):
    thumbs = ''.join(
        f'<button class="thumb{" is-on" if i == 1 else ""}" type="button" data-src="images/{u["id"]}-{i}.jpg" data-alt="{e(a)}" aria-label="Show photo: {e(a)}">'
        f'<img src="images/{u["id"]}-{i}.jpg" alt="" loading="lazy" width="1200" height="800"></button>'
        for i, a in enumerate(u['alts'], 1))
    perks = ''.join(f'<li>{e(p)}</li>' for p in u['perks'])
    tags = ''.join(f'<span class="tag">{e(t)}</span>' for t in u['tags'])
    note = f'<p class="note"><strong>Good to know.</strong> {e(u["note"])}</p>' if u['note'] else ''
    return f'''
    <article class="unit{" unit--flip" if flip else ""}" id="{u["id"]}">
      <div class="gallery">
        <div class="gallery__main"><img src="images/{u["id"]}-1.jpg" alt="{e(u["alts"][0])}" loading="lazy" width="1200" height="800">
          <span class="badge">{e(u["badge"])}</span></div>
        <div class="gallery__thumbs">{thumbs}</div>
      </div>
      <div class="unit__body">
        <p class="kicker">{e(u["kicker"])}</p>
        <h3>{e(u["name"])}</h3>
        <p class="specs">{e(u["specs"])}</p>
        <p class="rating"><span class="star" aria-hidden="true">★</span> <strong>{u["rating"]}</strong> · {u["reviews"]} reviews</p>
        <p class="blurb">{e(u["blurb"])}</p>
        <ul class="perks">{perks}</ul>
        <div class="tags">{tags}</div>
        {note}
        <div class="unit__cta">
          <a class="btn" href="{u["link"]}" target="_blank" rel="noopener">Check dates on Airbnb</a>
          <span class="price">from <strong>${u["price"]}</strong> a night</span>
        </div>
      </div>
    </article>'''

stays = ''
n = 0
for gid, gname, gsub, gdesc in GROUPS:
    stays += f'''
  <section class="group" id="{gid}">
    <header class="group__head">
      <p class="eyebrow">{e(gsub)}</p>
      <h2>{e(gname)}</h2>
      <p class="lede">{e(gdesc)}</p>
    </header>'''
    for u in UNITS:
        if u['group'] == gid:
            stays += unit_html(u, n % 2 == 1)
            n += 1
    stays += '\n  </section>'

rows = ''
T = {'garage': ('4', 'Full kitchen', 'Yes', 'Yes'), 'bunkhouse': ('4', 'Kitchenette', 'Yes', 'Yes'),
     'studio': ('6', 'Kitchenette', 'Yes', '–'), 'nook': ('2', 'Full kitchen', '–', 'Yes'),
     'cosmo': ('4', 'Full kitchen', '–', 'Yes'), 'cottage': ('8', 'Full kitchen', 'Yes', '–')}
for u in UNITS:
    s, k, p, ev = T[u['id']]
    rows += f'<tr><th scope="row"><a href="#{u["id"]}">{e(u["name"])}</a></th><td>{s}</td><td>{k}</td><td>{p}</td><td>{ev}</td><td>★ {u["rating"]}</td><td>${u["price"]}</td></tr>'

QUOTES = [
  ('Warm monkey bread stole the show!', 'George', 'The Studio'),
  ('Staying here is simply good for the soul.', 'Kelli', 'The Bunkhouse'),
  ('Bruce and Sue were beyond kind and gracious; we felt like family.', 'Alyssa', 'The Garage'),
  ('Possibly the best Airbnb we’ve stayed at.', 'Daniel', 'The Cottage'),
  ('Stop looking and book this place!', 'Pamela', 'The Cosmopolitan'),
  ('Could not have asked for a nicer place or a better host.', 'Marita', 'The Midnight Nook'),
]
quotes = ''.join(f'<figure class="quote"><blockquote>“{e(q)}”</blockquote><figcaption>{e(n_)} · {e(w)}</figcaption></figure>' for q, n_, w in QUOTES)

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Three Forks Accommodations · Pullman, WA</title>
<meta name="description" content="Six Superhost stays in Pullman, Washington, minutes from WSU. Farm animals, EV chargers, karaoke, and warm monkey bread at every check-in.">
<meta property="og:title" content="Three Forks Accommodations · Pullman, WA">
<meta property="og:description" content="Six Superhost stays near WSU. Every stay starts with warm monkey bread.">
<meta property="og:image" content="images/garage-1.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<a class="skip" href="#stays">Skip to the stays</a>
<header class="nav">
  <a class="brand" href="#top">Three Forks <span>Accommodations</span></a>
  <nav aria-label="Sections">
    <a href="#stays">Stays</a>
    <a href="weekend/">This weekend</a>
    <a href="#monkey-bread">Monkey bread</a>
    <a href="#animals">The animals</a>
    <a href="#groups">Groups</a>
    <a href="#reviews">Reviews</a>
  </nav>
</header>

<main id="top">
  <section class="hero">
    <img class="hero__img" src="images/farm-4.jpg" alt="Sunset over the Palouse behind a row of pines at the farm" width="1200" height="800">
    <div class="hero__inner">
      <p class="eyebrow">Pullman, Washington · minutes from WSU</p>
      <h1>Six places to stay in Pullman. One warm monkey bread welcome.</h1>
      <p class="hero__sub">Family-run stays from Bruce and Sue: two on our farm with mini Highland cows, three near downtown, and a restored 1930s cottage on Pioneer Hill.</p>
      <a class="btn btn--light" href="#stays">Find your stay</a>
    </div>
  </section>

  <section class="stats" aria-label="Host record on Airbnb">
    <div><strong>4.99</strong><span>average rating</span></div>
    <div><strong>257</strong><span>guest reviews</span></div>
    <div><strong>Superhost</strong><span>4 years hosting</span></div>
    <div><strong>6 of 6</strong><span>are Guest favorites</span></div>
    <div><strong>100%</strong><span>response rate, within the hour</span></div>
  </section>

  <div id="stays" class="stays">
    <nav class="jump" aria-label="Jump to a stay">
      {''.join(f'<a href="#{u["id"]}">{e(u["name"])}<small>Sleeps {T[u["id"]][0]}</small></a>' for u in UNITS)}
    </nav>
    {stays}
  </div>

  <section class="bread" id="monkey-bread">
    <div class="bread__photo"><img src="images/monkeybread-1.jpg" alt="Fresh monkey bread on a wooden cake stand" loading="lazy" width="1200" height="853"></div>
    <div class="bread__body">
      <p class="eyebrow">The welcome treat</p>
      <h2>Every stay starts with warm monkey bread.</h2>
      <p>One of your hosts loves to bake. So when you arrive, at any of our six places, there is homemade monkey bread waiting, often still warm from the oven. Some seasons it comes with another dessert, or even homemade ice cream.</p>
      <p>It is the thing guests write about most.</p>
      <div class="bread__quotes">
        <figure><blockquote>“Fresh hot monkey bread coordinated with my arrival!”</blockquote><figcaption>Sara · The Midnight Nook</figcaption></figure>
        <figure><blockquote>“I’ve never had a host bring by fresh anything, much less a monkey bread that was 10/10.”</blockquote><figcaption>Jennifer · The Cosmopolitan</figcaption></figure>
        <figure><blockquote>“Fresh monkey bread… and even homemade ice cream this time!”</blockquote><figcaption>Kelli · The Bunkhouse</figcaption></figure>
      </div>
    </div>
  </section>

  <section class="animals" id="animals">
    <header class="group__head">
      <p class="eyebrow">At The Garage and The Bunkhouse</p>
      <h2>Meet the neighbors.</h2>
      <p class="lede">Mini Highland cows, mini pigs and fainting goats live in the stables next to our two farm stays, and they love visitors. Treats for feeding are provided. Staying in town? Ask us about stopping by to say hello.</p>
    </header>
    <div class="mosaic">
      <img class="m1" src="images/farm-1.jpg" alt="A shaggy mini Highland cow in the paddock" loading="lazy" width="1200" height="800">
      <img src="images/farm-2.jpg" alt="Three goats leaning into the fence" loading="lazy" width="1200" height="800">
      <img src="images/farm-3.jpg" alt="A calf looking over the rail" loading="lazy" width="1200" height="800">
      <img src="images/farm-b-1.jpg" alt="Two Highland calves sharing hay" loading="lazy" width="1200" height="800">
      <img src="images/farm-5.jpg" alt="Fire pit ringed with log seats in the snow" loading="lazy" width="1200" height="800">
    </div>
  </section>

  <section class="groups" id="groups">
    <header class="group__head">
      <p class="eyebrow">Game weekends, graduation, family visits</p>
      <h2>Bringing a bigger group?</h2>
      <p class="lede">Our stays pair up. Message us on Airbnb and we will help you book them together.</p>
    </header>
    <div class="combos">
      <div class="combo"><span class="combo__n">8</span><h3>The Garage + The Bunkhouse</h3><p>Side by side on the same five acres, with the animals next door.</p></div>
      <div class="combo"><span class="combo__n">6</span><h3>The Cosmopolitan + The Midnight Nook</h3><p>Upstairs and downstairs in the same building on Walnut Street.</p></div>
      <div class="combo"><span class="combo__n">12</span><h3>All three Walnut Street stays</h3><p>Add The Studio, a three-minute walk up the street, for karaoke and movie night.</p></div>
      <div class="combo"><span class="combo__n">8</span><h3>The Cottage</h3><p>One house, three bedrooms, two living spaces. No coordination required.</p></div>
    </div>

    <div class="table-wrap">
      <table>
        <caption>All six stays at a glance</caption>
        <thead><tr><th scope="col">Stay</th><th scope="col">Sleeps</th><th scope="col">Kitchen</th><th scope="col">Pets</th><th scope="col">EV charger</th><th scope="col">Rating</th><th scope="col">From / night</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    <p class="fine">Rates are starting points and change with dates and season; Airbnb shows the exact price. Weekly and monthly discounts apply on every stay.</p>
  </section>

  <section class="reviews" id="reviews">
    <header class="group__head">
      <p class="eyebrow">257 reviews · 4.99 average</p>
      <h2>What guests say.</h2>
    </header>
    <div class="quotes">{quotes}</div>
  </section>

  <section class="know" id="good-to-know">
    <h2>Good to know</h2>
    <dl>
      <div><dt>Check-in and checkout</dt><dd>Check in from 3:00 PM, check out by 11:00 AM. Self check-in with a smart lock.</dd></div>
      <div><dt>Minimum stay</dt><dd>Two nights. Longer stays are welcome, with weekly and monthly discounts.</dd></div>
      <div><dt>Home base, not the after-party</dt><dd>Only registered guests stay overnight, and there are no gatherings, tailgates or watch parties. Want a friend to swing by? Just message us first.</dd></div>
      <div><dt>Cameras</dt><dd>Exterior security cameras cover the entrances. There are none inside.</dd></div>
      <div><dt>Pets</dt><dd>Welcome at The Garage, The Bunkhouse, The Studio and The Cottage.</dd></div>
      <div><dt>EV charging</dt><dd>Level 2 chargers at The Garage, The Bunkhouse, The Midnight Nook and The Cosmopolitan. Public chargers are scarce in Pullman.</dd></div>
    </dl>
  </section>
</main>

<footer class="footer">
  <p class="brand">Three Forks <span>Accommodations</span></p>
  <p>Hosted by Bruce and Sue in Pullman, Washington. Booking and messaging happen on Airbnb.</p>
  <p class="footer__links">{' · '.join(f'<a href="{u["link"]}" target="_blank" rel="noopener">{e(u["name"])}</a>' for u in UNITS)}</p>
  <p class="go">Go Cougs!</p>
</footer>
<script src="site.js"></script>
</body>
</html>
'''
open(sys.argv[1], 'w', encoding='utf-8').write(page)
print(len(page))
