class ArrayUtils
  def checar_duplicatas(array)
    array2 = []
    array3 = []
    for n in (0..array.length)
    array2 << array[0]
    array.delete_at(0)
    for i in (array)
      if array2[n] == i
        array3 << i
      end
    end
end
array3 = array3.uniq
array3
end
end
