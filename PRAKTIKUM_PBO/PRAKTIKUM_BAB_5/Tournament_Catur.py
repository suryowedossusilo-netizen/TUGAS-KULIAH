class Player:
    def __init__(self, nama, rating):
        self.nama = nama
        self.rating = rating
        self.poin = 0.0

    def __repr__(self):
        return f"Player({self.nama}, rating={self.rating}, poin={self.poin})"


class Match:
    def __init__(self, player1, player2, hasil):
        """
        hasil: 'menang' jika player1 menang, 'kalah' jika player1 kalah, 'seri'
        """
        self.player1 = player1
        self.player2 = player2
        self.hasil = hasil

        if hasil == "menang":
            player1.poin += 1.0
            player2.poin += 0.0
        elif hasil == "kalah":
            player1.poin += 0.0
            player2.poin += 1.0
        elif hasil == "seri":
            player1.poin += 0.5
            player2.poin += 0.5

    def __repr__(self):
        return f"Match({self.player1.nama} vs {self.player2.nama}, hasil={self.hasil})"


class Tournament:
    def __init__(self, nama):
        self.nama = nama
        self.players = []
        self.matches = []

    def addPlayer(self, player):
        self.players.append(player)
        print(f"Pemain {player.nama} (Rating: {player.rating}) ditambahkan")

    def addMatch(self, match):
        self.matches.append(match)
        print(f"Pertandingan ditambahkan: {match}")

    def getRanking(self):
        ranking = sorted(self.players, key=lambda p: (-p.poin, -p.rating))
        return ranking

    def displayRanking(self):
        ranking = self.getRanking()
        print(f"\n=== PERINGKAT TURNAMEN: {self.nama} ===")
        print(f"{'Rank':<6}{'Nama':<15}{'Rating':<10}{'Poin':<10}")
        print("-" * 40)
        for i, p in enumerate(ranking, 1):
            print(f"{i:<6}{p.nama:<15}{p.rating:<10}{p.poin:<10}")

    def displayMatches(self):
        print(f"\n=== DAFTAR PERTANDINGAN ===")
        for i, m in enumerate(self.matches, 1):
            if m.hasil == "menang":
                hasil_str = f"{m.player1.nama} menang"
            elif m.hasil == "kalah":
                hasil_str = f"{m.player2.nama} menang"
            else:
                hasil_str = "Seri"
            print(f"{i}. {m.player1.nama} vs {m.player2.nama} -> {hasil_str}")

print("=" * 50)
print("TUGAS 2: TOURNAMENT CATUR")
print("=" * 50)

tournament = Tournament("Grand Prix 2026")

p1 = Player("Magnus", 2850)
p2 = Player("Hikaru", 2800)
p3 = Player("Fabiano", 2780)
p4 = Player("Ding", 2760)

tournament.addPlayer(p1)
tournament.addPlayer(p2)
tournament.addPlayer(p3)
tournament.addPlayer(p4)

tournament.addMatch(Match(p1, p2, "menang"))
tournament.addMatch(Match(p3, p4, "seri"))
tournament.addMatch(Match(p1, p3, "menang"))
tournament.addMatch(Match(p2, p4, "kalah"))
tournament.addMatch(Match(p1, p4, "seri"))
tournament.addMatch(Match(p2, p3, "menang"))

tournament.displayMatches()
tournament.displayRanking()
