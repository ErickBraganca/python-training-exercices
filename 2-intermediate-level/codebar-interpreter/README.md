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
            <li>Routine Code.</li>
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
    <li>Product Type:
        <ul>
            <li>Joias: 001.</li>
            <li>Livros: 111.</li>
            <li>Eletrônicos: 333.</li>
            <li>Bebidas: 555.</li>
            <li>Brinquedos: 888.</li>
        </ul>
    </li>
</ol>

## 🏅 Restrictions
<ul>
    <li>Não há produtos fora das especificações acima</li>
    <li>Não é possível despachar joias com origem no Centro-Oeste</li>
    <li>O vendedor 367 está com o CNPJ inválido, portanto não pode enviar pacotes</li>
</ul>

## 🏅 Goals
- [ ] HTML - Identificar a região de destino de cada pacote totalizando-os.
- [ ] HTML - Saber quais tem códigos inválidos.
- [ ] HTML - Identificar os pacotes que tem como origem a região sul e brinquedos.
- [ ] HTML - Listar pacotes agrupados por região de destino.
- [ ] HTML - Listar pacotes agrupados por vendedor.
- [ ] HTML - Listar pacotes inválidos.


