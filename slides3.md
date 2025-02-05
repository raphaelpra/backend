class: middle, slide_title

<img class="slide_title_mpt" src="static/media/logos/logo_mines_paris.png">
<img class="slide_title_cnrs" src="static/media/logos/logo_cnrs.jpg">

<!-- <img class="slide_title_armines" src="static/media/logos/logo_armines.jpg"> -->
<img class="left_panel" src="static/media/logos/mines_paris_lampe.png">

# Programmes coopérants 🚀

## Framework web --- Flask !

<p> <strong><i>Basile Marchand</i></strong><sup> 1</sup></p>

.footnote[1 - Plateforme SISDev, Centre des Matériaux, MINES Paris - CNRS - Université PSL]

---

layout: true
<img class="slide_header_mpt" src="static/media/logos/logo_mines_paris.png">
<img class="slide_header_cnrs" src="static/media/logos/logo_cnrs.jpg">

<!-- <img class="slide_header_armines" src="static/media/logos/logo_armines.jpg"> -->

<div class="slide_footer">
    <div class="wrap">
        <span>2025 - <i> Flask </i>  </span>
    </div>
</div>

---

# Récap des épisodes précédents

.center[Architecture classique Client <-> Serveur avec des variations peer-to-peer, three-tier, ... ]

.cols[
.fifty[
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1188.9763249545028 1606.6407791513025" height="500">

  <!-- svg-source:excalidraw -->

  <defs>
    <style class="style-fonts">
      @font-face {
        font-family: "Virgil";
        src: url("https://excalidraw.com/Virgil.woff2");
      }
      @font-face {
        font-family: "Cascadia";
        src: url("https://excalidraw.com/Cascadia.woff2");
      }
    </style>
  </defs>
  <rect x="0" y="0" width="1188.9763249545028" height="1606.6407791513025" fill="#ffffff"></rect><g stroke-linecap="round" transform="translate(10 10) rotate(0 581.5030339661319 334.33439324541473)"><path d="M32 0 M32 0 C290.86 6, 548.72 6.44, 1131.01 0 M1131.01 0 C1151.03 2.67, 1166.35 14.3, 1163.01 32 M1163.01 32 C1159.95 181.96, 1161.7 336.03, 1163.01 636.67 M1163.01 636.67 C1164.4 657, 1148.6 669.24, 1131.01 668.67 M1131.01 668.67 C705.86 675.47, 284.52 672.94, 32 668.67 M32 668.67 C8.91 665.02, 1.11 658.37, 0 636.67 M0 636.67 C-0.99 410.64, -1.41 188.43, 0 32 M0 32 C2.07 8.31, 8.4 1.13, 32 0" stroke="#e67700" stroke-width="4.5" fill="none" stroke-dasharray="8 12"></path></g><g stroke-linecap="round" transform="translate(200.4341160350998 48.34475720453929) rotate(0 457.49996185302734 96.99997901916504)"><path d="M1.43 1.06 C267.01 3.67, 532.68 3.22, 915.61 -0.07 M0.67 0.33 C339.03 -2.79, 678.03 -4.05, 915.63 0.59 M911.98 -1.35 C919.73 75.86, 919.83 152.79, 916.04 191.34 M914.4 1.87 C914.43 71.39, 913.45 143.45, 914.7 192.1 M914.95 192.48 C585.72 190.6, 253.68 192.01, 0.49 195.02 M914.21 194.16 C720.89 194.89, 528.22 194.1, -0.45 194.37 M1.41 192.99 C-4.47 145.03, -4.66 100.45, -2.65 -1.01 M1.98 193.12 C2.44 123.31, 3.96 50.78, -0.57 -0.3" stroke="#e67700" stroke-width="2" fill="none"></path></g><g transform="translate(300.50471921939106 77.89198009091706) rotate(0 166.5 22.5)"><text x="0" y="32" font-family="Virgil, Segoe UI Emoji" font-size="36px" fill="#e67700" text-anchor="start" style="white-space: pre;" direction="ltr">Couche 1 : physique</text></g><g transform="translate(277.43414655267793 137.84477627802562) rotate(0 288 35)"><text x="0" y="25" font-family="Virgil, Segoe UI Emoji" font-size="28px" fill="#e67700" text-anchor="start" style="white-space: pre;" direction="ltr">Transmission de signaux</text><text x="0" y="60" font-family="Virgil, Segoe UI Emoji" font-size="28px" fill="#e67700" text-anchor="start" style="white-space: pre;" direction="ltr">Emission réception d'un ou plusieurs bit(s)</text></g><g stroke-linecap="round" transform="translate(209.22831059332316 475.0464711832542) rotate(0 457.49996185302734 96.99997901916504)"><path d="M-0.85 1.05 C327.35 4.33, 651.57 3.91, 916.23 0.62 M0.7 0.73 C299.3 3.75, 597.81 2.67, 915.56 -0.39 M911.27 0.95 C909.33 57.04, 911.78 118.3, 912.89 191.84 M916.59 1.41 C917.25 56.95, 917.92 117.18, 914.64 194.83 M916.03 193.66 C731.52 201.62, 546.11 200.04, -0.29 194.26 M914.71 194.48 C612.22 186.49, 309.89 187.07, 0.03 193.72 M1.45 191.4 C3.87 156.73, -0.95 115.88, -1.96 -1.99 M1.41 195.62 C-0.51 122.2, -1.09 47.7, 1.3 1.95" stroke="#e67700" stroke-width="2" fill="none"></path></g><g transform="translate(309.2989137776142 504.5936940696324) rotate(0 165 22.5)"><text x="0" y="32" font-family="Virgil, Segoe UI Emoji" font-size="36px" fill="#e67700" text-anchor="start" style="white-space: pre;" direction="ltr">Couche 3 : réseau</text></g><g transform="translate(286.2283411109013 564.5464902567405) rotate(0 250 35)"><text x="0" y="25" font-family="Virgil, Segoe UI Emoji" font-size="28px" fill="#e67700" text-anchor="start" style="white-space: pre;" direction="ltr">Communication de proche en proche </text><text x="0" y="60" font-family="Virgil, Segoe UI Emoji" font-size="28px" fill="#e67700" text-anchor="start" style="white-space: pre;" direction="ltr">Routage et adressage des paquets</text></g><g stroke-linecap="round" transform="translate(202.06400216663496 262.50532119152695) rotate(0 457.49996185302734 96.99997901916504)"><path d="M-0.77 -1.31 C275.29 -0.14, 547.4 -0.83, 916.22 -0.39 M-0.06 -0.79 C280.02 -5.34, 559.58 -5.88, 914.95 -0.64 M912.88 1.99 C914.91 39.77, 911.32 80.02, 917.41 191.34 M916.84 -1.16 C917.75 41.14, 916.1 81.11, 916.58 194.64 M916.27 193.28 C724.55 191.36, 532.33 189.42, -0.1 193.91 M915.1 194.14 C729.54 194.82, 543.56 195.13, 0.1 194.28 M-2.98 190.46 C-2.68 133.63, -4.52 76.24, 2.03 -0.43 M1.11 193.94 C-3.59 134.57, -2.01 72.83, -1.07 -0.06" stroke="#e67700" stroke-width="2" fill="none"></path></g><g transform="translate(302.134605350926 292.05254407790426) rotate(0 157.5 22.5)"><text x="0" y="32" font-family="Virgil, Segoe UI Emoji" font-size="36px" fill="#e67700" text-anchor="start" style="white-space: pre;" direction="ltr">Couche 2 : liaison</text></g><g transform="translate(279.0640326842131 352.0053402650133) rotate(0 404.5 35)"><text x="0" y="25" font-family="Virgil, Segoe UI Emoji" font-size="28px" fill="#e67700" text-anchor="start" style="white-space: pre;" direction="ltr">interface réseau </text><text x="0" y="60" font-family="Virgil, Segoe UI Emoji" font-size="28px" fill="#e67700" text-anchor="start" style="white-space: pre;" direction="ltr">communication entre deux machines directement connectées</text></g><g stroke-linecap="round" transform="translate(211.6164134022183 699.5281352194611) rotate(0 457.49996185302734 96.99997901916504)"><path d="M0.43 0.1 C321.36 1.32, 640.33 1.68, 916.26 0.01 M0.58 0.08 C205.25 -4, 409.72 -3.04, 915.04 -0.33 M912.45 -3.05 C910.78 55.22, 909.88 104.08, 917.02 196.11 M916.17 0.37 C913.46 57.85, 914.36 117.05, 916.4 193.62 M913.43 194.28 C596.71 190.07, 280.34 189.25, 0.33 195.15 M915.71 194.36 C556.82 197.44, 199.96 196.28, 0.19 194.16 M-3.41 190.65 C-5.91 118.29, -3 43.15, -2.67 -0.66 M-1.55 195.76 C3.89 149.11, 3.5 105.43, 0.43 0.5" stroke="#1864ab" stroke-width="2" fill="none"></path></g><g transform="translate(311.68701658650934 729.0753581058393) rotate(0 188.5 22.5)"><text x="0" y="32" font-family="Virgil, Segoe UI Emoji" font-size="36px" fill="#1864ab" text-anchor="start" style="white-space: pre;" direction="ltr">Couche 4 : transport</text></g><g transform="translate(288.61644391979644 789.0281542929474) rotate(0 210.5 17.5)"><text x="0" y="25" font-family="Virgil, Segoe UI Emoji" font-size="28px" fill="#1864ab" text-anchor="start" style="white-space: pre;" direction="ltr">Communication entre processus</text></g><g stroke-linecap="round" transform="translate(209.22831059332248 928.7860048734606) rotate(0 457.49996185302734 96.99997901916504)"><path d="M-1.25 -0.42 C279.44 -6.38, 556.57 -5.12, 914.57 1.03 M0.1 0.73 C250.82 6.12, 502.49 5.06, 915.32 -0.76 M912.1 -2.18 C918.67 47.85, 914.92 96.93, 913 194.53 M913.07 1.59 C913.84 53.11, 913.08 103.79, 914.87 194.94 M914.62 193.94 C569.79 187.67, 226.6 187.19, -0.76 194.66 M915.47 194.43 C676.73 201.08, 437.31 200.35, -0.28 194.11 M2.94 193.6 C3.58 140.4, 4.15 81.64, 1.58 0.38 M-0.6 194.52 C3.86 119.13, 3.11 43.75, -1.15 1.4" stroke="#1864ab" stroke-width="2" fill="none"></path></g><g transform="translate(309.2989137776135 958.333227759837) rotate(0 164.5 22.5)"><text x="0" y="32" font-family="Virgil, Segoe UI Emoji" font-size="36px" fill="#1864ab" text-anchor="start" style="white-space: pre;" direction="ltr">Couche 5 : session</text></g><g transform="translate(286.2283411109006 1018.2860239469469) rotate(0 220.5 35)"><text x="0" y="25" font-family="Virgil, Segoe UI Emoji" font-size="28px" fill="#1864ab" text-anchor="start" style="white-space: pre;" direction="ltr">Synchronisation des échanges </text><text x="0" y="60" font-family="Virgil, Segoe UI Emoji" font-size="28px" fill="#1864ab" text-anchor="start" style="white-space: pre;" direction="ltr">Ouverture/fermeture de session</text></g><g stroke-linecap="round" transform="translate(211.61641340221854 1158.0438745274591) rotate(0 457.49996185302734 96.99997901916504)"><path d="M-1 0.58 C311.01 7.45, 624.94 6.48, 915.34 -0.91 M-0.37 0.35 C331.9 4.14, 663.17 3.82, 915.32 -0.37 M918.54 -2.07 C915.57 77.47, 912.33 150.64, 917.61 197.61 M914.45 1.33 C918.32 54.33, 915.92 106.67, 916.04 194.91 M915.37 193.85 C705.89 199.87, 497.82 201.93, 0.75 193.14 M914.23 194.48 C652.16 193.04, 389.53 193.6, 0.06 193.34 M1.78 197.18 C-2.73 122.93, -6.19 55.96, 0.92 -3.03 M-0.16 192.67 C-3.3 149.46, -1.72 103.32, -1.03 0.69" stroke="#1864ab" stroke-width="2" fill="none"></path></g><g transform="translate(311.68701658650957 1187.5910974138355) rotate(0 214 22.5)"><text x="0" y="32" font-family="Virgil, Segoe UI Emoji" font-size="36px" fill="#1864ab" text-anchor="start" style="white-space: pre;" direction="ltr">Couche 6 : présentation</text></g><g transform="translate(288.61644391979667 1247.5438936009455) rotate(0 227 17.5)"><text x="0" y="25" font-family="Virgil, Segoe UI Emoji" font-size="28px" fill="#1864ab" text-anchor="start" style="white-space: pre;" direction="ltr">Encodage/Décodage des données</text></g><g stroke-linecap="round" transform="translate(214.00451621111415 1383.4894570844876) rotate(0 457.49996185302734 96.99997901916504)"><path d="M-1.16 0.02 C313.55 5.46, 628.86 6.35, 914.4 -0.12 M0.72 -0.61 C356.65 -5.67, 711.49 -5.4, 915.07 -0.35 M917.94 -1.76 C912.09 61.4, 914.26 129.85, 916.13 194.02 M914.16 -1.9 C910.61 43.66, 913 89.76, 914.86 195.94 M914.59 192.58 C644.97 192.65, 374.7 193.87, 1.03 193.77 M915.43 194.36 C635.92 191.57, 358.55 191.56, -0.18 194.45 M3.4 190.74 C1.12 153.11, 4.66 109.49, 0.92 2.06 M-1.04 195.84 C3.46 131.09, 1.09 64.96, 1.75 1.55" stroke="#1864ab" stroke-width="2" fill="none"></path></g><g transform="translate(314.0751193954052 1413.036679970864) rotate(0 193.5 22.5)"><text x="0" y="32" font-family="Virgil, Segoe UI Emoji" font-size="36px" fill="#1864ab" text-anchor="start" style="white-space: pre;" direction="ltr">Couche 7 : application</text></g><g transform="translate(291.0045467286923 1472.989476157974) rotate(0 146 17.5)"><text x="0" y="25" font-family="Virgil, Segoe UI Emoji" font-size="28px" fill="#1864ab" text-anchor="start" style="white-space: pre;" direction="ltr">L'application réseau </text></g><g stroke-linecap="round" transform="translate(1016.7123606947414 1435.697376910803) rotate(0 44.71341429421955 38.20964494233294)"><path d="M57.35 7.02 L87.94 41.64 L74.41 46.36 L48.47 73.57 L14.83 45.85 L2.78 40.8 L6.48 28.95 L40.45 5.89 L43.2 1.31 L57.41 8.64" stroke="none" stroke-width="0" fill="#228be6"></path><path d="M56.25 9.75 M56.25 9.75 C65.3 16.01, 66.95 23.63, 78.18 29.25 M56.25 9.75 C63.38 14.73, 69.16 19.69, 78.18 29.25 M78.18 29.25 C85.59 40.83, 88.07 41.2, 78.18 48.75 M78.18 29.25 C88.31 40.15, 89.24 35.3, 78.18 48.75 M78.18 48.75 C67.52 52.94, 64.68 60.82, 56.25 66.67 M78.18 48.75 C71.62 54.77, 68.54 56.97, 56.25 66.67 M56.25 66.67 C47.86 72.96, 45.02 78.85, 33.75 66.67 M56.25 66.67 C41.65 79.21, 40.66 73.49, 33.75 66.67 M33.75 66.67 C29.46 59.39, 18.08 55.42, 11.25 48.75 M33.75 66.67 C23.72 61.12, 16.97 54.28, 11.25 48.75 M11.25 48.75 C-0.21 37, -2.87 39.46, 11.25 29.25 M11.25 48.75 C-4.29 37.66, 3.44 39.48, 11.25 29.25 M11.25 29.25 C18.4 22.38, 26.08 21.93, 33.75 9.75 M11.25 29.25 C16.83 23.52, 21.89 19.94, 33.75 9.75 M33.75 9.75 C41.63 0.71, 47.29 -1.82, 56.25 9.75 M33.75 9.75 C44.42 4.02, 46.93 2.66, 56.25 9.75" stroke="#1864ab" stroke-width="4" fill="none"></path></g><g transform="translate(1053.885295333876 1447.0384722005042) rotate(0 12.595744680851112 27.57446808510622)"><text x="0" y="39.148936170212785" font-family="Virgil, Segoe UI Emoji" font-size="44.02194635353149px" fill="#fff" text-anchor="start" style="white-space: pre;" direction="ltr">7</text></g><g stroke-linecap="round" transform="translate(1018.4399244288361 1211.2157128745953) rotate(0 44.71341429421955 38.20964494233294)"><path d="M58.68 13.02 L87.69 39.73 L74.96 45.84 L47.84 74.12 L10.65 49.52 L4.32 40.02 L6.62 34.52 L43.7 2.97 L45.7 1.47 L58.92 5.79" stroke="none" stroke-width="0" fill="#228be6"></path><path d="M56.25 9.75 M56.25 9.75 C59.53 13.18, 70.16 23.07, 78.18 29.25 M56.25 9.75 C64.11 14.75, 67.26 22.15, 78.18 29.25 M78.18 29.25 C89.62 40.3, 88.09 41.87, 78.18 48.75 M78.18 29.25 C92.93 39.65, 88.85 42.77, 78.18 48.75 M78.18 48.75 C69.94 52.98, 65.23 58.66, 56.25 66.67 M78.18 48.75 C69.29 56.31, 62.1 62.19, 56.25 66.67 M56.25 66.67 C42.56 77.74, 43.22 73.89, 33.75 66.67 M56.25 66.67 C43.47 75.88, 41.2 75.04, 33.75 66.67 M33.75 66.67 C30.21 63.8, 22.94 55.49, 11.25 48.75 M33.75 66.67 C25.64 62.55, 19.88 56.69, 11.25 48.75 M11.25 48.75 C0.84 35.6, 3.81 40.75, 11.25 29.25 M11.25 48.75 C-4.22 39.87, -0.2 42.75, 11.25 29.25 M11.25 29.25 C14.38 21.46, 22.49 19.28, 33.75 9.75 M11.25 29.25 C18.02 23.02, 26.9 15.74, 33.75 9.75 M33.75 9.75 C41.57 2.78, 45.61 2.75, 56.25 9.75 M33.75 9.75 C44.81 -1.58, 48.79 -1.81, 56.25 9.75" stroke="#1864ab" stroke-width="4" fill="none"></path></g><g transform="translate(1055.612859067971 1222.5568081642964) rotate(0 15 27.5)"><text x="0" y="39" font-family="Virgil, Segoe UI Emoji" font-size="44.02194635353149px" fill="#fff" text-anchor="start" style="white-space: pre;" direction="ltr">6</text></g><g stroke-linecap="round" transform="translate(1020.8280272377319 981.9578432205976) rotate(0 44.71341429421955 38.20964494233294)"><path d="M53.14 8.51 L87.45 35.6 L81.98 50.5 L41.33 74.74 L11.08 52.01 L1.38 37.04 L7.29 29.48 L40.18 2.06 L47.45 5.58 L52.66 10.59" stroke="none" stroke-width="0" fill="#228be6"></path><path d="M56.25 9.75 M56.25 9.75 C62.81 10.65, 68.35 18.74, 78.18 29.25 M56.25 9.75 C65.97 16.31, 73.85 24.94, 78.18 29.25 M78.18 29.25 C90.84 40.53, 89.94 39.52, 78.18 48.75 M78.18 29.25 C85.68 42.2, 91.15 43.59, 78.18 48.75 M78.18 48.75 C70.92 52.62, 65.13 55.16, 56.25 66.67 M78.18 48.75 C72.62 55.63, 66.44 60.54, 56.25 66.67 M56.25 66.67 C45.61 73.32, 42.97 72.94, 33.75 66.67 M56.25 66.67 C45.09 75.81, 42.69 76.18, 33.75 66.67 M33.75 66.67 C28.72 66.28, 23.13 54.9, 11.25 48.75 M33.75 66.67 C27.21 62, 21.84 60.71, 11.25 48.75 M11.25 48.75 C-1.27 36.89, 1.73 40.32, 11.25 29.25 M11.25 48.75 C-3.46 41.61, -0.95 35.69, 11.25 29.25 M11.25 29.25 C16.7 19.85, 22.74 19.11, 33.75 9.75 M11.25 29.25 C15.24 24.52, 23.69 21.09, 33.75 9.75 M33.75 9.75 C43.09 0.38, 41.72 -1.81, 56.25 9.75 M33.75 9.75 C43.85 2.08, 44.11 -2.29, 56.25 9.75" stroke="#1864ab" stroke-width="4" fill="none"></path></g><g transform="translate(1058.0009618768668 993.2989385102987) rotate(0 14.5 27.5)"><text x="0" y="39" font-family="Virgil, Segoe UI Emoji" font-size="44.02194635353149px" fill="#fff" text-anchor="start" style="white-space: pre;" direction="ltr">5</text></g><g stroke-linecap="round" transform="translate(1018.4399244288363 759.8642819932866) rotate(0 44.71341429421955 38.20964494233317)"><path d="M55.72 7.74 L86.4 36.6 L76.8 48.45 L45.24 77.93 L11.31 45.62 L-0.59 42.89 L11.07 29.78 L40.42 -0.88 L49.84 1.63 L54.14 11.48" stroke="none" stroke-width="0" fill="#228be6"></path><path d="M56.25 9.75 M56.25 9.75 C62.44 13.12, 72.39 23.91, 78.18 29.25 M56.25 9.75 C59.2 16.16, 64.85 17.4, 78.18 29.25 M78.18 29.25 C86.36 36.03, 88.15 42.71, 78.18 48.75 M78.18 29.25 C90.27 36.8, 89.87 35.23, 78.18 48.75 M78.18 48.75 C71.73 51.52, 65.47 54.79, 56.25 66.67 M78.18 48.75 C69.71 53.67, 65 61.91, 56.25 66.67 M56.25 66.67 C44.84 75.96, 45.9 79.25, 33.75 66.67 M56.25 66.67 C42.12 73.93, 46.61 77.26, 33.75 66.67 M33.75 66.67 C28.59 62.87, 18.36 59.12, 11.25 48.75 M33.75 66.67 C27.24 62.76, 20.73 57.88, 11.25 48.75 M11.25 48.75 C-3.77 42.6, 3.51 38.01, 11.25 29.25 M11.25 48.75 C4.31 36.73, 3.55 34.91, 11.25 29.25 M11.25 29.25 C16.85 21.82, 29.24 18.39, 33.75 9.75 M11.25 29.25 C17.89 21.3, 26.77 18.1, 33.75 9.75 M33.75 9.75 C44.27 -3.12, 44.07 -1.46, 56.25 9.75 M33.75 9.75 C48.88 4.1, 45.82 -0.71, 56.25 9.75" stroke="#1864ab" stroke-width="4" fill="none"></path></g><g transform="translate(1055.612859067971 771.2053772829877) rotate(0 15 27.5)"><text x="0" y="39" font-family="Virgil, Segoe UI Emoji" font-size="44.02194635353149px" fill="#fff" text-anchor="start" style="white-space: pre;" direction="ltr">4</text></g><g stroke-linecap="round" transform="translate(1013.6637188110449 525.8302067214954) rotate(0 44.71341429421955 38.20964494233317)"><path d="M52.53 9.31 L89.45 37.88 L81.06 44.98 L48.6 77.49 L10.26 52.49 L0.84 42.09 L4 35.3 L39.75 6.23 L44.11 3.06 L57.27 13.71" stroke="none" stroke-width="0" fill="#fd7e14"></path><path d="M56.25 9.75 M56.25 9.75 C61.39 12.05, 72.03 23.72, 78.18 29.25 M56.25 9.75 C61.39 17.03, 70.08 21.19, 78.18 29.25 M78.18 29.25 C88.81 41.74, 89.68 39.23, 78.18 48.75 M78.18 29.25 C93.29 37.96, 90.26 39.39, 78.18 48.75 M78.18 48.75 C69.42 51.72, 65.1 61.02, 56.25 66.67 M78.18 48.75 C70.32 52.61, 64.01 60.26, 56.25 66.67 M56.25 66.67 C42.97 79.48, 44.64 76.13, 33.75 66.67 M56.25 66.67 C47.35 72.86, 41.37 74.17, 33.75 66.67 M33.75 66.67 C22.79 59.11, 19.22 51.08, 11.25 48.75 M33.75 66.67 C26.07 61.61, 22.41 57.73, 11.25 48.75 M11.25 48.75 C-2.49 35.67, -1.03 37.03, 11.25 29.25 M11.25 48.75 C-0.52 35.83, 2.92 34.49, 11.25 29.25 M11.25 29.25 C18.18 23.95, 29.72 12.06, 33.75 9.75 M11.25 29.25 C16.51 26.11, 21.97 20.17, 33.75 9.75 M33.75 9.75 C45.16 1.58, 48.04 -3.4, 56.25 9.75 M33.75 9.75 C44.2 -3.58, 44.85 -1.62, 56.25 9.75" stroke="#e67700" stroke-width="4" fill="none"></path></g><g transform="translate(1050.8366534501797 537.1713020111983) rotate(0 16 27.5)"><text x="0" y="39" font-family="Virgil, Segoe UI Emoji" font-size="44.02194635353149px" fill="#fff" text-anchor="start" style="white-space: pre;" direction="ltr">3</text></g><g stroke-linecap="round" transform="translate(1008.887513193253 315.67715953866445) rotate(0 44.71341429421955 38.20964494233317)"><path d="M52.92 8.72 L84.65 38.55 L75.42 51.29 L41.08 76.08 L14.68 52.02 L2.14 40.94 L10.5 29.41 L39.37 4.76 L48.64 4.19 L58.62 12.38" stroke="none" stroke-width="0" fill="#fd7e14"></path><path d="M56.25 9.75 M56.25 9.75 C65.23 11.44, 67.42 17, 78.18 29.25 M56.25 9.75 C63.12 17.21, 70.38 22.82, 78.18 29.25 M78.18 29.25 C86.07 38.9, 89.48 41.21, 78.18 48.75 M78.18 29.25 C90.04 42.06, 90.53 34.72, 78.18 48.75 M78.18 48.75 C69.55 51.88, 63.38 56.77, 56.25 66.67 M78.18 48.75 C71.5 55.5, 65.03 60.89, 56.25 66.67 M56.25 66.67 C43.52 72.6, 41.83 75.67, 33.75 66.67 M56.25 66.67 C44.99 76.38, 46.48 77.56, 33.75 66.67 M33.75 66.67 C27.34 62.78, 22.6 58.01, 11.25 48.75 M33.75 66.67 C29.47 60.69, 23.14 59.8, 11.25 48.75 M11.25 48.75 C1.1 39.06, 2.73 36.9, 11.25 29.25 M11.25 48.75 C3.61 39.88, -2.31 37.78, 11.25 29.25 M11.25 29.25 C16.15 23.26, 30.65 12.03, 33.75 9.75 M11.25 29.25 C19.71 24.16, 28.56 16.21, 33.75 9.75 M33.75 9.75 C47.02 -1.29, 47.78 3.94, 56.25 9.75 M33.75 9.75 C47.73 1.67, 48.26 -3.25, 56.25 9.75" stroke="#e67700" stroke-width="4" fill="none"></path></g><g transform="translate(1046.0604478323878 327.01825482836557) rotate(0 16.5 27.5)"><text x="0" y="39" font-family="Virgil, Segoe UI Emoji" font-size="44.02194635353149px" fill="#fff" text-anchor="start" style="white-space: pre;" direction="ltr">2</text></g><g stroke-linecap="round" transform="translate(1011.2756160021481 100.74790673804046) rotate(0 44.71341429421955 38.20964494233317)"><path d="M52.43 6.58 L85.87 38.99 L78.15 50.04 L45.99 75.11 L11.1 51.78 L3.77 40.65 L11.16 35.25 L40.79 6.17 L48.16 6.11 L52.96 11.48" stroke="none" stroke-width="0" fill="#fd7e14"></path><path d="M56.25 9.75 M56.25 9.75 C67.77 15.36, 76.87 25.95, 78.18 29.25 M56.25 9.75 C60.42 13.01, 65.48 19.54, 78.18 29.25 M78.18 29.25 C92.78 35.17, 92.58 42.36, 78.18 48.75 M78.18 29.25 C85.76 39.61, 93.88 40.38, 78.18 48.75 M78.18 48.75 C73.06 59.15, 64.57 63.27, 56.25 66.67 M78.18 48.75 C69.73 54.13, 62.28 62, 56.25 66.67 M56.25 66.67 C48.77 79.62, 45.9 80.17, 33.75 66.67 M56.25 66.67 C41.45 79.82, 48.4 77.24, 33.75 66.67 M33.75 66.67 C29.52 56.43, 18.25 53.87, 11.25 48.75 M33.75 66.67 C25.26 61.47, 21.25 55.47, 11.25 48.75 M11.25 48.75 C-3.35 37.25, -2.38 37.23, 11.25 29.25 M11.25 48.75 C2.71 43.2, 1.89 35.33, 11.25 29.25 M11.25 29.25 C21.77 24.46, 26.41 12.89, 33.75 9.75 M11.25 29.25 C19.18 24.16, 27.17 14.27, 33.75 9.75 M33.75 9.75 C47.66 -3.15, 45.6 1.68, 56.25 9.75 M33.75 9.75 C48.52 -3.59, 45.53 -1.02, 56.25 9.75" stroke="#e67700" stroke-width="4" fill="none"></path></g><g transform="translate(1048.448550641283 112.08900202774157) rotate(0 7 27.5)"><text x="0" y="39" font-family="Virgil, Segoe UI Emoji" font-size="44.02194635353149px" fill="#fff" text-anchor="start" style="white-space: pre;" direction="ltr">1</text></g><g stroke-linecap="round" transform="translate(15.970257022239139 686.7736089619962) rotate(0 581.5030339661319 454.93358509465315)"><path d="M32 0 M32 0 C408.08 8.61, 787.13 9.73, 1131.01 0 M1131.01 0 C1155.22 1.15, 1160.46 13.71, 1163.01 32 M1163.01 32 C1161.73 240.2, 1160.98 445.43, 1163.01 877.87 M1163.01 877.87 C1160.9 895.73, 1155.33 910.54, 1131.01 909.87 M1131.01 909.87 C697.73 906.41, 262.3 905.77, 32 909.87 M32 909.87 C12.08 906.09, -3.37 898.14, 0 877.87 M0 877.87 C2.43 602.09, 2.66 324.85, 0 32 M0 32 C-1.45 10.7, 9.76 -3.74, 32 0" stroke="#1864ab" stroke-width="4.5" fill="none" stroke-dasharray="8 12"></path></g><g transform="translate(-204.86916546137502 325.4166960915377) rotate(270.05441647727315 304.06837457447324 23.912436963854816)"><text x="0" y="33.82487392770985" font-family="Virgil, Segoe UI Emoji" font-size="38.234424889863895px" fill="#e67700" text-anchor="start" style="white-space: pre;" direction="ltr">Couches inférieures "matérielles"</text></g><g transform="translate(-221.97559336675715 1132.626948600408) rotate(270.05441647727315 330.00000000000006 24)"><text x="0" y="34" font-family="Virgil, Segoe UI Emoji" font-size="38.234424889863895px" fill="#1864ab" text-anchor="start" style="white-space: pre;" direction="ltr">Couches supérieures "applicatives" </text></g></svg>
]
.fifty[
Un modèle OSI en 7 couches

.center[<img src="static/media/adresseip.png" width="30%">]

Un protocole HTTP(S) pour le web

.center[
<img src="static/media/http_request.png" width="60%">
]

]
]

<div style="position: absolute; bottom: 5%; left: 40%;">
<img src="static/media/serveur_recap.png" width="400px">
</div>

<div style="position: absolute; bottom: 15%; left: 80%;">
<img src="static/media/logos/letsencrypt.png" width="200px">
</div>

<div style="position: absolute; bottom: 0%; left: 75%;">
<p style="font-size: 4rem"> 🍪 </p>
</div>

---

# Les framework

Réponse à un besoin mais lequel ?

.center[***Cadre de développement simplifié***]

En gros un guide <strike> spirituel </strike>, permettant de développer simplement des applications spécifiques.

.center[

<iframe src="https://giphy.com/embed/MZW5o8f5RaH0Q" width="480" height="197" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

]

---

# Framework vs Librairie

.center[Frameworks, Librairies, même chose ? <br> ]

--

.cols[
.fifty[
.center[<b> Librairies </b>]

Ensemble de programmes effectuant des opérations spécifiques, que vous allez utiliser de manière ponctuelle au sein de vos programmes en suivant votre propre logique.

<br>

Par exemple `NumPy` en Python 🐍 est une librairie

.center[
<img src="static/media/library.png" width="70%">
]

]
.vertbar[]
.fifty[
.center[<b> Framework </b>]

Cadre de développement dans lequel le développeur vient s'inscrire, i.e. développer des fonctionnalités/comportements. Là ce n'est plus le développeur qui fixe sa logique mais le framework.

<br>

Un code à trou 🕳️ en quelque sorte

.center[
<img src="static/media/framework_concept.png" width="70%">
]

]
]

---

# Frontend, backend

.center[⚠️ Framework web un terme très, trop, générique ⚠️]

.cols[
.fifty[

.center[Framework frontend]

.center[

  <img src="static/media/framework_frontend.png" width=50%>
]

Focalisé sur le développement d'application côté client.

]
.vertbar[]
.fifty[

.center[Framework backend]

.center[

  <img src="static/media/framework_backend.png" width=100%>
]

Focalisé sur le développement côté serveur

]
]

Dans le cadre de ce cours on ne se focalisera que sur le côté `backend`

---

# Les grands principes des framework backend

.center[
<img src="static/media/framework_routes.png" width=100%>
]

A cela un framework complet ajoute des fonctionnalités de :
.center[`Web Template`, `Sécurité`, `Accès à des bases de données`]

---

# Framework Flask

Micro-framework Python 🐍 développé depuis 2010.
<br><br>
.center[
<img src="static/media/logos/logo_flask.png" width=40% />
]
<br><br>
🚧 Micro-framework ne veut pas dire pas utilisable sur des gros projets ⚠️
<br><br>
.center[
Pinterest, Airbnb, Trivago, ...
]
<br><br>
Micro-framework car noyau très léger et minimaliste mais pouvant être enrichi avec des extensions.

---

# Pourquoi Flask et pas autre chose

1️⃣ Vous savez tous a peu prêt faire du Python 🐍

.center[donc on élimine tout ce qui n'est pas à base Python]

--

2️⃣ On va essayer de vous apprendre des trucs utilisés par ailleurs

.center[

<figure>
<img src="static/media/web_framework_survey.png" width="60%"/><br>
<label style="font-size: x-small"> Source: <a href="https://www.jetbrains.com/lp/devecosystem-2022/python/">https://www.jetbrains.com/lp/devecosystem-2022/python/</a>
</figure>
]

--

3️⃣ Pourquoi Flask et pas Django

.center[J'ai une séance de 3 heures pas un semestre ... <span style="font-size: xx-small">et puis j'aime pas Django</span> 😒]

---

class: middle, center

# Mais au fait ...

# ... pourquoi on s'intéresse à ça ?

---

# Graphical User Interface

Faire le pont 🌉 entre :

.center[un code de calcul/traitement de donnée/...

et

une interface graphique
]

Deux approches :

.cols[
.fifty[
.center[***Old school***]

Utilisation de librairies graphiques et développement d'un client lourd

.center[
<img src="static/media/qt_fltk.png" width=50%>
]

]
.vertbar[]
.fifty[
.center[***New age***]

Utilisation du navigateur

.center[
<img src="static/media/html_css_js.png" width=80%>
]

]
]

<div style="transform: rotate(40deg); opacity: 0.9;position: absolute; right: 10%; top: 25%; border: 1px solid darkblue; border-radius: 10px; padding: 2pt 10pt; background-color: aliceblue;">
<p style="opacity: 1; color: crimson; font-weight: bold; background-color: aliceblue"> Projets d'informatique ... </p>
</div>

---

# Une première app

## Installation

Pour commencer on installe `Flask`

```bash
pip install flask
```

Vous pourrez alors travailler en local 💻️. <br>
<br>
Au besoin si vous voulez vous mettre dans une configuration serveur vous pouvez utiliser [@Replit](https://replit.com) il y a un template Flask.
<br><br>
.center[Et rien de plus à faire 😯 <br>
<br><br>
c'est l'avantage de Flask par rapport à Django <br> qui nécessite un setup plus poussé pour démarrer un projet]

---

# Minimal Working Example

- Step 1️⃣ :

```python
from flask import Flask
```

- Step 2️⃣

```python
app = Flask("Appli de ouf")
```

Ensuite tout repose sur une syntaxe un peu particulière :

```python
*@app.route("/une/url/cible")
def la_fonction_correspondante():
  // fait des trucs très intelligents
  // et encore plus
  return un_resultat ## pouvant être du html, du json, ....

```

Pour finir :

.cols[
.fifty[

```python
app.run(debug=True, port=3001)
```

]
.fifty[
`debug=True` permet d'activer du hot reloading
]
]

---

# Pour ceux qui auraient la flemme !

.cols[
.sixty[
.center[<iframe src="https://giphy.com/embed/4KkSbPnZ5Skec" width="471" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>]

]
.fourty[
[http://bit.ly/3Z5C5k7](http://bit.ly/3Z5C5k7)

.center[<img src="static/media/qrcode/flask_sandbox.png" width="60%">]
]
]

---

# Envoyer autre choses qu'une chaine !

Si on veut pour une url donnée renvoyer non pas une chaîne mais un fichier HTML qui lui même peut nécessiter des CSS/JS il va falloir une organisation un peu particulière

.cols[
.fifty[

```bash
.
├── app.py
├── static
│   ├── css
│   │   └── wheel.css
│   └── js
│       └── wheel.js
└── templates
    └── wheel.html
```

]
.fifty[

```python
from flask import render_template
```

```python
@app.route("/")
def index():
  return render_template("wheel.html")
```

]
]

En revanche tous les fichiers contenus dans le dossier `static` seront automatiquement accessible sans que l'on ait rien à faire et ça c'est 🆒 !

---

# Un truc un tout petit peu plus évolué

## Passage de paramètres aux URLs

.center[
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 894.5550217693453 62.253204331505" width="894.5550217693453" height="62.253204331505">

  <!-- svg-source:excalidraw -->

  <defs>
    <style class="style-fonts">
      @font-face {
        font-family: "Virgil";
        src: url("https://excalidraw.com/Virgil.woff2");
      }
      @font-face {
        font-family: "Cascadia";
        src: url("https://excalidraw.com/Cascadia.woff2");
      }
    </style>
  </defs>
  <rect x="0" y="0" width="894.5550217693453" height="62.253204331505" fill="#ffffff"></rect><g stroke-opacity="0.5" fill-opacity="0.5" stroke-linecap="round" transform="translate(563.4306688499037 10) rotate(0 160.56217645972083 21.1266021657525)"><path d="M9.71 0.16 L309.96 -0.1 L316.84 -0.96 L321.95 4.75 L321.58 30.23 L317.86 40.37 L312.22 42.39 L9.17 40.82 L3.37 38.43 L-0.95 31.91 L1.11 6.32 L6.88 -0.5 L11.55 -1.22" stroke="none" stroke-width="0" fill="#fd7e14"></path><path d="M10.56 0 M10.56 0 C81.63 -2.25, 156.35 -2.17, 310.56 0 M10.56 0 C81.14 0.56, 152.22 0.23, 310.56 0 M310.56 0 C318.62 1.46, 320.87 2.48, 321.12 10.56 M310.56 0 C316.16 -1.25, 319 3.37, 321.12 10.56 M321.12 10.56 C319.2 16.52, 321.66 19.52, 321.12 31.69 M321.12 10.56 C320.63 16.16, 321.31 23.33, 321.12 31.69 M321.12 31.69 C322.47 40.41, 316.29 41.97, 310.56 42.25 M321.12 31.69 C323.38 36.71, 317.38 41.49, 310.56 42.25 M310.56 42.25 C197.91 41.5, 85.79 42.26, 10.56 42.25 M310.56 42.25 C247.92 40.66, 186.11 40.51, 10.56 42.25 M10.56 42.25 C1.94 44.04, -0.42 39.17, 0 31.69 M10.56 42.25 C3.24 41.7, -1.32 37.43, 0 31.69 M0 31.69 C0.2 26.68, 1.75 19.96, 0 10.56 M0 31.69 C0.47 26.38, -0.45 18.84, 0 10.56 M0 10.56 C1.2 5.23, 5.13 0.59, 10.56 0 M0 10.56 C-1.79 3.36, 3.23 1.46, 10.56 0" stroke="#e67700" stroke-width="4" fill="none"></path></g><g stroke-opacity="0.9" fill-opacity="0.9" transform="translate(10 14.32660216575232) rotate(0 429.7877502441406 16.799999999999955)"><text x="0" y="0" font-family="Virgil, Segoe UI Emoji" font-size="28px" fill="#000000" text-anchor="start" style="white-space: pre;" direction="ltr" dominant-baseline="text-before-edge">https://domain-name.fr/une/route/donnée?name=Basile&amp;age=32</text></g></svg>
]

Besoin de récupérer dans la fonction `handler` la requête et donc ses arguments 🤔

.center[Flask a tout prévu]

.cols[
.sixty[

```python
from flask import request

@app.route("/une/route/donnee")
def handler():
  name = request.args.get("name")
  age = request.args.get("age")
  return f"<h1> Hello {name} ! Tu as vraiment {age} ans ? </h1>"
```

]
.fourty[
⚠️ Si l'argument n'existe pas la fonction `get` retourne `None`
]
]

.center[🚧 Pas de notion de type dans les arguments, tout est chaîne de caractère 🚧]

---

# URL paramétrique

Possibilité offerte par Flask de définir des paramètres au sein même d'une URL

.center[
<img src="static/media/route_param.png" width=70%>
]

.cols[
.fifty[
Possibilité de typer les paramètres :

- `string` : pour tout texte sans slash
- `int` : valeur entière positive
- `float` : valeur flottante positive
- `path` : comme les string mais accepte les slashs

]
.fifty[

```python
@app.route("/home/<int:user_id>")
def home_uid(user_id):
    ## do something according to user_id value
    return ""
```

]
]

---

# Un exemple : générateur de nombre aléatoire

API de génération de nombres aléatoires

- `/api/integer` : génère des entiers
- `/api/float` : génère des flottant

Possibilité pour les deux d'ajouter un paramètre `n` par exemple `?n=10` pour générer 10 valeurs alétoires.

.center[
[http://bit.ly/3nb0yaG](http://bit.ly/3nb0yaG)
]

.center[
<img src="static/media/qrcode/flask_random_api.png" width="20%">
]

---

# Une API complète

Petit rappel du 1er épisode, HTTP différentes requêtes possibles

- `GET` : requêtes pour **_obtenir_** du serveur une ressource (fichier html/css/js, image, video, données, ...)
- `POST` : requêtes pour **_envoyer_** des données au serveur en vu d'un traitement (ajout d'un utilisateur dans une base de donnée, ...)
- `PATCH` : requêtes pour **_modifier partiellement_** une ressource du serveur (mettre à jour l'addresse mail d'un utilisateur dans la base de donnée)
- `DELETE` : requêtes pour **_supprimer_** une ressource du serveur (supprimer un commentaire sur un article, ... )

Il s'agit là des principaux types de requêtes mais il en existe d'autre, pour la liste complète vous pouvez faire un tour [https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol).

.center[<img src="static/media/api_img.jpg" width="40%">]

.footnote[Image from Jérémy Mésière, Architecte Middleware chez Manutan]

---

# Spécification des requêtes

Une fonction pour un chemin mais pour différent type de requête

```python
from flask import request

@app.route("/chemin", methods=['GET', 'POST'])
def the_function():
  if request.method == "POST":
    ## do something for post
    return post_response
  elif request.method == "GET":
    ## do other thing
    return get_response
```

Une fonction par chemin et par type de requête

```python
@app.get("/chemin")
def get_for_chemin():
  return

@app.post("/chemin")
def post_for_chemin():
  return
```

---

# Récupérer les données reçue

.center[Encore une fois tout se passe dans `request`]

Plusieurs méthodes à disposition :

- `request.is_json()` pour vérifier qu'il y a bien du json dans la requête
- `request.get_json()` qui retourne le contenu de la requête

.center[
⚠️ Lorsque vous traitez une requête `POST` il faut impérativement que votre fonction renvoie quelque chose ⚠️
]

[http://bit.ly/40ly786](http://bit.ly/40ly786)

.center[
<img src="static/media/qrcode/flask_post.png" width="20%">
]

---

# Servir des pages HTML

Deux cas de figures :

- Fichiers "statiques" -> contenu ne dépendant de rien donc le plus simple en fait

.center[<iframe src="https://giphy.com/embed/Rl9Yqavfj2Ula" width="400" height="300" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>]

--

- Fichiers "dynamiques" -> contenu dépendant de données externes (base de données typiquement, paramètres utilisateur... )

.center[Page profil utilisateur, liste de produits disponibles, ... ]

---

# Fichies dynamique : CSR vs SSR

Pour le cas de pages dynamiques deux approches existent

.center[
**C**lient **S**ide **R**endering
<br><br> vs <br><br>
**S**erver **S**ide **R**endering
]

.center[<iframe src="https://giphy.com/embed/QYMBnZjnxko0eCzBuF" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
]

---

# Une démo

.center[
[http://bit.ly/3Tx8wqL](http://bit.ly/3Tx8wqL)
]

.center[
<img src="static/media/qrcode/flask_ssr_vs_csr.png" width="30%">
]

Il faut être curieu et ouvrir l'onglet "Network" des outils de développement du navigateur !

---

# Approche CSR

.center[<img src="static/media/csr.png" width=80%>]

---

# Approche SSR

.center[
<img src="static/media/ssr.png" width=75%>
]

.center[
Besoin d'un mécanisme de ***génération de page HTML***
]

---

# Moteur de template

Mécanisme de génération de page HTML à partir d'un modèle et de données.

.center[
<img src="static/media/template_engine.png" width="50%">
]

Plusieurs techno/solutions :

.center[***Jinja2***, **Pug**, **Mustache**, **Ejs**]

---

# Jinja 2

Moteur de template Pythonique 🐍

Lien avec Flask via la fonction `render_template`

```python
from flask import render_template
```

Que l'on utilise dans les fonctions de routage

```python
@app.route("/")
def index():
  context = {}
  ### do something
  return render_template("templated_html.html", **context)
```

Où `context` est un dictionnaire Python contenant les variables que l'on souhaite transmettre de notre application Flask au moteur de template.

---

# Jinja 2

## Substitution de variables

Pour afficher dans le HTML le contenu d'une variable il faut entourer cette dernière par des doubles accolades dans du code HTML.

```html
<div>Bonjour {{ name }}</div>
```

---

# Jinja 2

## Blocs conditionnels

Pour choisir d'afficher ou nom une partie de la page HTML vous pouvez utiliser des branchements de type _if_, _else if_, _else_. La syntaxe est la suivante

```html
{% if une_condition %}
<div>du html en pagaille</div>
{% elif une_autre_condition %}
<div>un autre fouilli de html</div>
{% else %}
<div>le html par défaut</div>
{% endif %}
```

_Remarque_ le `None` de Python se transforme en `none` dans Jinja2

---

# Jinja 2

## Boucles for

L'intérêt majeur étant l'affichage dynamique de tableau. Les boucles for dans Jinja2 vous permettent d'itérer sur tout objet Python iterable. La syntaxe est la suivante

```html
{% for x in ma_liste %}
<div>Iteration {{ x }}</div>
{% endfor %}
```

---

# Synthèse CSR vs SSR

Deux modes avec des avantages et inconvénients

Grosso modo

- CSR c'est cool pour

.center[Avoir des pages avec beaucoup d'interaction,<br><br>notamment lorsque l'on est plus sur de l'appli web que du site web]

- SSR c'est bien pour

.center[accélérer le chargement initial de votre site, si vous avez peu d'interaction avec l'utilisateur,<br><br>si vous souhaitez optimiser votre référencement naturel dans les moteurs de recherches.]

Et d'un point de vue très pragmatique
.center[peut dépendre également du confort que vous avez à programmer en Python ou Javascript]

---

# Jinja2 plein d'autres choses

On a survolé les fonctionnalités de base de Jinja mais il y a plein de trucs advance super pratiques

[https://jinja.palletsprojects.com/en/3.1.x/templates/](https://jinja.palletsprojects.com/en/3.1.x/templates/)

Liste non exhaustive :

- Composition de template par héritage
- Définition de macro

---

# Gestion des formulaires avec Flask

Un truc récurrent dans le web c'est les formulaires :

- Authentification
- Messagerie
- Interface utilisateur
- ...

<br><br>
Un besoin

.center[Spécifier les champs (nom et nature/type) ; agréger les données saisies par l'utilisateur ; envoyer ces données au backend ; traiter ces données et émettre une réponse ]

Un module tout fait en Python WTForm et son interface pour Flask FlaskWTF

```bash
pip install flask-wtf
```

<div style="position: absolute; top: 22%; left: 25%">
<iframe src="https://giphy.com/embed/26FPJGjhefSJuaRhu" width="480" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</div>
<div style="position: absolute; top: 13%; right: 8%">
<iframe src="https://giphy.com/embed/xT5LMUv1JAxBiCft4I" width="480" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</div>

---

# Principes

L'utilisation de Flask-WTF se fait en définissant son propre formulaire en créant une classe héritant de la class `FlaskForm`.

```python
from flask_wtf import FlaskForm
```

Par exemple un formulaire de login pourrait s'écrire de la manière suivante :

```python
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
```

---

# Les types input

.cols[
.fifty[
Les différents types prédéfinis dans `WTForm` sont les suivants :

- `BooleanField` : représente un booléen
- `DateField` : représente une date
- `FileField` : pour la sélection de fichier
- `MultipleFileField` : pour la sélection multiple
- `FloatField`
- `IntegerField`
- `DecimalField`
- `SelectField` : choix parmi une liste d'option
- `SubmitField` : le bouton de soumission du formulaire
- `PasswordField` : champs pour le mot de passe (affiche des étoiles)
- `TextAreaField` : champs de saisie de texte libre
  ]
  .fifty[

Possibilité d'ajouter des "validateurs"

- `DataRequired` : champs obligatoire
- `Email` : le champs est une adresse email
- `EqualTo` : test d'égalité
- `NumberRange` : valeur numérique dans un intervalle
- `Optional` : champs optionnel

]
]

--

<div style="position: absolute; bottom: 10%; right: 5%; transform: rotate(20deg)">
<iframe src="https://giphy.com/embed/lPF1CyJXXcTZmUrP2J" width="480" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</div>

---

# Utilisation en lien avec les templates

.cols[
.fifty[

```html
<html>
  <head>
    <title>Flask WTF</title>
  </head>
  <body>
    <hr />
    <h1>Sign In</h1>
    <form action="" method="post" novalidate>
      {{ form.hidden_tag() }}
      <p>
        {{ form.username.label }}<br />
        {{ form.username(size=32) }}
      </p>
      <p>
        {{ form.password.label }}<br />
        {{ form.password(size=32) }}
      </p>
      <p>{{ form.submit() }}</p>
    </form>
  </body>
</html>
```

]
.fifty[
La méthode `form.hidden_tag` va générer une ligne du genre :

```html
<input
  id="csrf_token"
  name="csrf_token"
  type="hidden"
  value="ImI0ODg5NjE3NzdiYjM5NWJlZWRiYzE3MDlmZjBhNjFkMDhlMjE4M2Ii.Xq_IiQ.GG9q2vWBhqbZGuGGJue2MwDIQwI"
/>
```

Auncun intérêt fonctionnel. En revanche utile pour la sécurité 🚨 et se prémunir des attaques type
<br><br>
.center[**C**ross **S**ite **R**equest **F**orgery]

]
]

---

# Données du formulaire dans les `handler`

On peut directement réutiliser la classe `LoginForm` dans nos fonctions handler par exemple :

```python
@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        "Log in requested for {form.username.data} with passord {form.password.data}")
        ## Add function here to check password

        return redirect("/home")
    return render_template("login.html", form=form)
```

[http://bit.ly/3JyTBb2](http://bit.ly/3JyTBb2)

.center[<img src="static/media/qrcode/flask_form.png" width="20%">]

---

# Un petit bonus : les Cookies 🍪

.cols[
.fifty[

```python
@app.route('/route/install/cookie')
def handler():

  resp = make_response(render_template('mapage.html'))
  resp.set_cookie('cookie', "eat me")

  return resp
```

]
.fifty[

```python
@app.route('/route/read/cookie')
def handler():
   name = request.cookies.get('cookieName')
   # ...
```

]
]

Par exemple, nombre de fois qu'on visite une page !

[http://bit.ly/408GbcF](http://bit.ly/408GbcF)

.center[
<img src="static/media/qrcode/flask_cookie.png" width="20%">
]

---

# Un mot sur la notion de `Session`

Très souvent besoin de la notion de session utilisateur

.center[Stocker des infos spécifiques à un utilisateur entre deux requêtes]

Possible de faire ça à la main 🖖🏻 à l'aide de cookies 🍪 ...

.center[mais Flask peut tout faire à votre place]

.cols[
.fourty[

```python
from Flask import session
```

Besoin d'un peu de config par contre

```python
app.config["SECRET_KEY"] = "un secret"
```

[http://bit.ly/3JYyboX](http://bit.ly/3JYyboX)
]
.sixty[

```python

@app.route("/une/url/<string:username>")
def handler( username ):
  session["name"] = username
  return "Ok j'ai enregistré"

@app.route("/")
def index():
  name = session.get("name")
  if name:
    return f"Hello {name}"
  else:
    return "Merci de faire d'abord une requête vers /une/url/<username>"
```

]
]

<div style="position: absolute; top: 10%; right: 5%">
<img src="static/media/qrcode/flask_session_demo.png" width="200px">
</div>

---

# Et les websocket ...

Petit rappel au cas où ...

.cols[
.fifty[
<br><br>
.center[connexion **bidirectionnelle** entre un client et le serveur
<br><br>on parle de connexion *full-duplex*
<br><br>Permet au serveur de ***pousser*** des informations vers le client sans que ce dernier n'est rien demandé 😲
]
]
.fifty[
.center[<img src="static/media/ws.png" width="70%">]
]
]

---

# Utilisation des Websocket

Un module dédié dans Flask

```bash
pip install flask-socketio
```

L'utilisation de websocket avec Flask se fait de manière très simple. Il suffit tout d'abord de créer notre serveur websocket à l'aide de la classe `SocketIO` que l'on attache à notre application Flask.

```python
from flask_socketio import SocketIO
socketio = SocketIO(app)
```

Ensuite rien de révolutionnaire on enregistre des fonctions pour des `events` donnés

```python
@socketio.on('message')
def handle_message(json):
    print('received my event: ' + str(json))
    socketio.emit('my response', json)
```

---

# Exemple de Chat Flask + SocketIO

.cols[
.fifty[

```python
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

@socketio.on('receive_msg')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socketio.emit('the_response', json)

```

.center[
Possibilité d'ajouter par dessus la notion de `room` <br><br>
pour une gestion plus fine des destinataires
<br><br>
📥️ 📤️
<br><br>
[http://bit.ly/3yVAEdt](http://bit.ly/3yVAEdt)
]
]
.fifty[

```js
let socket = io.connect("http://" + document.domain + ":" + location.port);
$("form").on("submit", (e) => {
  e.preventDefault();
  let user_name = $("input.username").val();
  let user_input = $("input.message").val();
  socket.emit("receive_msg", {
    user_name: user_name,
    message: user_input,
  });
  $("input.message").val("").focus();
});
socket.on("the_response", (msg) => {
  if (typeof msg.user_name !== "undefined") {
    $("h3").remove();
    $("div.message_holder").append(
      '<div><b style="color: #000">' +
        msg.user_name +
        "</b> " +
        msg.message +
        "</div>"
    );
  }
});
```

]

]

<div style="position: absolute; bottom: 5%; left: 40%">
<img src="static/media/qrcode/flask_socketio.png" width="200px">
</div>

---

# Tout ce qu'on ne peut pas voir

.center[🚀 Cours en mode express 🚀]

Plein de choses que l'on ne peut pas voir :

.center[Authentification, gestion de base de données,<br><br>sécurité des applications web, interface avec services externes, ... ]

**Quelques ressources**

.center[
[https://flask.palletsprojects.com/en/1.1.x/](https://flask.palletsprojects.com/en/1.1.x/)

[https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
]

---

# Juste un mot quand même sur l'aspect Base de Données

Pour faire de la base de donnée relationnelle simplement

.center[SQLAlchemy]

Avec une intégration Flask assez simple via `Flask-SQLAlchemy`

Après dans le cas où vous avez besoin d'une base de données `simple` pour faire de la lecture/écriture minimaliste une solution :

.center[Passer par un service externe]

Trucs à la mode : Notion ou Airtable par exemple

---

# Flask SQLAlchemy

```bash
pip install Flask-SQLAlchemy
```

.center[
Gestion de base de données se fait via des **modèles**
<br><br>
vous allez voir c'est beaucoup plus simple que ce qu'on vous a dit en prépa 😅
]

---

# Utilisateur

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
```

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy(app)

```

Pour initializer la base de donnée

```python
db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.add(User(username="bob", email="bob.leponge@maison-ananas.com"))
    db.session.add(User(username="patrick", email="patrick.etoile@maison-ananas.com"))

*   db.session.commit()
```

---

# Interogation de la base de donnée

**Liste de tous les utilisateurs**

```python
@app.route("/list")
def list():
*   users = User.query.all()
    output = [f"{user.username} ({user.email})" for user in users]
    return "<pre><code>" + "<br>".join(output) + "</pre></code>"
```

**Recherche d'un utilisateur**

```python
@app.route("/get/<string:username>")
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return "<h1>User not found</h1>"
    return f"<h1>{user.username} ({user.email})</h1>"
```

---

# Posts

Ajout d'une classe Post (besoin d'une relation un Post est lié à un utilisateur)

```python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
*   user = relationship("User", back_populates="posts")
```

Besoin d'ajouter également une relation dans la classe User

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
*   posts = relationship("Post", back_populates="user")
```

---

# Utilisation

```python
@app.route("/posts")
def posts():
    posts = Post.query.all()
    output = [f"{post.title} ({post.content}) from {post.user.username}" for post in posts]
    return "<pre><code>" + "<br>".join(output) + "</pre></code>"

@app.route("/post/<string:username>")
def get_posts(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return "<h1>User not found</h1>"
    posts = user.posts
    output = [f"{post.title} ({post.content})" for post in posts]
    return "<pre><code>" + "<br>".join(output) + "</pre></code>"
```

.center[Ainsi toute la science occulte de la base de donnée relationnelle
<br><br>est cachée derrière des classes Python 🐍]

---

class: middle

# Dans le prochain épisode ...

--

.center[

<iframe src="https://giphy.com/embed/Xd6Y9TuDtylt5ug5PC" width="480" height="260" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
]
```
