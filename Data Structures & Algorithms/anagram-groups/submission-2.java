class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> output = new HashMap<>();

        for (String string : strs) {
            char[] charArray = string.toCharArray();
            Arrays.sort(charArray);
            String sortedS = new String(charArray);

            output.putIfAbsent(sortedS, new ArrayList<>());
            output.get(sortedS).add(string);
        }

        return new ArrayList<>(output.values());
    }
}
