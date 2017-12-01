import ExUnit.Assertions

defmodule PartII do
  @double for n <- ?a..?z, x <- ?a..?z, do: to_string([n, x])
  @triple for n <- ?a..?z, x <- ?a..?z, do: to_string([n, x, n])

  def contains_two_double(word) do
    !!Enum.find @double, false, &(length(String.split(word, &1)) > 2)
  end

  def contains_triplet(word) do
    !!Enum.find @triple, false, &(String.contains?(word, &1))
  end

  def nice?(word) do
    contains_two_double(word) && contains_triplet(word)
  end
end

assert PartII.nice?("qjhvhtzxzqqjkmpb")
assert PartII.nice?("xxyxx")
refute PartII.nice?("uurcxstgmygtbstg")
refute PartII.nice?("ieodomkazucvgmuy")

"../inputs/day_05.txt" 
|> File.read! 
|> String.trim 
|> String.split("\n")
|> Enum.map(&(PartII.nice?(&1)))
|> Enum.filter(&(&1 === true))
|> length
|> IO.puts
