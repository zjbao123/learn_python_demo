#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zjbao123'
'''
Given an array of strings, return all groups of strings that are anagrams.

Example:

Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

Note:

All inputs will be in lower-case'''

class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        Dict = {}
        result = []
        for string in strs:
            if ''.join(sorted(string)) not in Dict.keys():
                Dict[''.join(sorted(string))] = 1
            else:
                Dict[''.join(sorted(string))] += 1

        for string in strs:
            if Dict[''.join(sorted(string))] > 1:
                result.append(string)

        return result


print Solution().anagrams(['da', 'ba', 'ab', 'ad', 'cd'])
