<h1 align = "justify">🚦 BARCODE Interpreter</h1>

## 📜 Motivation
<span style="margin-botton: 5px">
The main motivation is the development of python algorithm to improve my understanding of the language and its resources.
</span>

## 🎯 Description
<span style="margin-botton: 5px">
The development of a barcode interpreter capable to perform the right interpretation of a code, composed of fifteen (15) digits, where each numerical triplet represents a specific information.
</span>

## 🏅 Barcode Structure
<ol>
    <li>Order of numerical triplets:
        <ul>
            <li>Região de Origem.</li>
            <li>Região de Destino.</li>
            <li>Company Code.</li>
            <li>Código do Vendedor do Produto.</li>
            <li>Tipo do produto.</li>
        </ul>
    </li>
    <li>Reference Code: City/Region
        <ul>
            <li>Centro-Oeste: 201 até 299.</li>
            <li>Nordeste: 300 até 399.</li>
            <li>Sudeste: 001 até 099.</li>
            <li>Sul: 100 até 199.</li>
        </ul>
    </li>
        <li>Reference Code: Vendor
        <ul>
            <li>123: Lojas A</li>
            <li>584: Lojas B</li>
            <li>124: Lojas C</li>
            <li>874: Lojas D</li>
            <li>654: Lojas E</li>
            <li>367: Lojas F</li>
        </ul>
    </li>
    <li>Product Type:
        <ul>
            <li>Joias: 001.</li>
            <li>Livros: 111.</li>
            <li>Eletrônicos: 333.</li>
            <li>Bebidas: 555.</li>
            <li>Brinquedos: 888.</li>
        </ul>
    </li>
    <li>Codes for Processing:</li>
    <br>Pacote 1:  288355555123888
    <br>Pacote 2:  335333555584333
    <br>Pacote 3:  223343555124001
    <br>Pacote 4:  002111555874555
    <br>Pacote 5:  111188555654777
    <br>Pacote 6:  111333555123333
    <br>Pacote 7:  432055555123888
    <br>Pacote 8:  079333555584333
    <br>Pacote 9:  155333555124001
    <br>Pacote 10: 333188555584333
    <br>Pacote 11: 555288555123001
    <br>Pacote 12: 111388555123555
    <br>Pacote 13: 288000555367333
    <br>Pacote 14: 066311555874001
    <br>Pacote 15: 110333555123555
    <br>Pacote 16: 333488555584333
    <br>Pacote 17: 455448555123001
    <br>Pacote 18: 022388555123555
    <br>Pacote 19: 432044555845333 
    <br>Pacote 20: 034311555874001
</ol>

## 🏅 Goals
- [X] HTML - Identificar a região de destino de cada pacote totalizando-os.
- [X] HTML - Saber quais tem códigos inválidos.
- [X] HTML - Listar pacotes agrupados por região de destino.
- [X] HTML - Listar pacotes agrupados por vendedor.
- [X] HTML - Listar pacotes inválidos.


