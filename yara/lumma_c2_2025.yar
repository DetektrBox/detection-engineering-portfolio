// yara/lumma_c2_2025.yar
rule LummaC2_2025 {
  meta:
    author = "Christopher Bradford"
    date = "2025-11-23"
    description = "LummaC2 stealer 2025 variants"
    mitre = "T1555.003"
  strings:
    $s1 = "LummaC2" ascii wide
    $s2 = "AppData\\Local\\Microsoft\\Windows\\INetCache" ascii
    $s3 = "passwords.txt" ascii
  condition:
    uint16(0) == 0x5a4d and 2 of them
}

// yara/asyncrat_2025.yar
rule AsyncRAT_2025 {
  meta:
    author = "Christopher Bradford"
    description = "AsyncRAT 2025 family"
  strings:
    $pdb = "AsyncRAT.pdb" ascii
    $str1 = "AsyncClient" ascii
    $str2 = "Ping" ascii wide
  condition:
    uint16(0) == 0x5a4d and 2 of them
}

// yara/pikabot_2025.yar
rule Pikabot_2025 {
  meta:
    author = "Christopher Bradford"
    description = "Pikabot loader/dropper 2025"
  strings:
    $s1 = "Pikabot" ascii nocase
    $s2 = "http://pikabot" ascii
  condition:
    any of them
}

// yara/latentit_2025.yar
rule Latentit_2025 {
  meta:
    author = "Christopher Bradford"
  strings:
    $s1 = "Latentit" ascii wide
    $s2 = "C:\\Users\\Public\\Latentit" ascii
  condition:
    any of them
}

// yara/qakbot_remnants_2025.yar
rule QakBot_Remnants_2025 {
  meta:
    author = "Christopher Bradford"
  strings:
    $mutex = "QakBot_Mutex_2025" ascii
  condition:
    $mutex
}

// yara/redline_stealer.yar
rule RedLine_Stealer {
  meta:
    author = "Christopher Bradford"
  strings:
    $s1 = "RedLineStealer" ascii wide
    $s2 = "Telegram" ascii
  condition:
    any of them
}

// yara/generic_lolbin_rundll32.yar
rule Generic_LOLBIN_Rundll32 {
  meta:
    author = "Christopher Bradford"
    description = "Suspicious rundll32 with no arguments"
  strings:
    $cmd = "rundll32.exe" wide
  condition:
    uint16(0) == 0x5a4d and $cmd and filesize < 2MB
}