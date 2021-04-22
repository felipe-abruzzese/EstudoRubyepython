class Word
  def anagrama?(uma_palavra, outra_palavra)
    arr_uma_palavra = uma_palavra.split('')
    arr_outra_palavra = outra_palavra.split('')
    arr_uma_palavra = arr_uma_palavra.map { |string| string.downcase  }
    arr_outra_palavra = arr_outra_palavra.map { |string| string.downcase  }
    arr_soma = arr_uma_palavra & arr_outra_palavra

    if arr_soma.length == arr_outra_palavra.length
      true
    else
      false
    end
  end
end
