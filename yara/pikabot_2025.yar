rule Pikabot_2025_Core_Strings {
    meta:
        author = "Christopher Bradford"
        description = "Detects Pikabot 2025 core loader strings"
        date = "2025-11-23"
        hash = "multiple 2025 samples"
    strings:
        $s1 = "Pikabot" ascii wide
        $s2 = "botnet_id=" ascii
        $s3 = "camp_id=" ascii
        $s4 = "http://185.117.73.132/" ascii
        $s5 = "http://193.233.132.51/" ascii
        $s6 = "Content-Type: application/x-www-form-urlencoded" ascii
        $s7 = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)" ascii
        $s8 = "PikabotC2" ascii
    condition:
        uint16(0) == 0x5A4D and 4 of them
}