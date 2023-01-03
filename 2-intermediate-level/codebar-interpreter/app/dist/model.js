const BAR_CODE_DUMMY = {
    getRegion: (key) => {
        if (key >= 1 || key <= 99) {
            return { Name: 'Sudeste', Code: [key] };
        } else if (key >= 100 || key <= 199) {
            return { Name: 'Sul', Code: [key] };
        } else if (key >= 201 || key <= 299) {
            return { Name: 'Centro-Oeste', regionCode: [key] };
        } else if (key >= 300 || key <= 399) {
            return { Name: 'Nordeste', Code: [key] };
        } else {
            return { Name: undefined, Code: [key] };
        }
    },
    getProductType: (key) => {
        switch (key) {
            case '001':
                return { Type: 'Joias', Code: [key] };
            case '111':
                return { Type: 'Livros', Code: [key] };
            case '333':
                return { Type: 'Eletrônicos', Code: [key] };
            case '555':
                return { Type: 'Bebidas', Code: [key] };
            case '888':
                return { Type: 'Brinquedos', Code: [key] };
            default:
                break;
        }
    }
}