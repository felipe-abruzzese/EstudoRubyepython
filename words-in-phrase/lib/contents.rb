class Contents
  def can_make_sentence?(contents)

    array_frase = contents[-1].split
    contents.pop
    array_palavras = contents

    array_frase = array_frase.map { |string| string.downcase  }
    array_palavras = array_palavras.map { |string| string.downcase  }

    array_resposta = array_frase & array_palavras

    if array_resposta.length == array_frase.length
      true
    else
      false
      end

  end
end
