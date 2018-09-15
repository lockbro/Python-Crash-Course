def CountryAndNation(country, nation, population=''):
    if population:
        return str(country.title() +
                   ',' +
                   nation.title() +
                   ' - population ' +
                   str(population))
    else:
        return str(country.title() +
                   ',' +
                   nation.title())
