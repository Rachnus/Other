using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using System;
using System.Collections.Generic;

namespace SieveOfEratosthenes
{
    /// <summary>
    /// This is the main type for your game.
    /// </summary>
    public class SieveOfEratosthenes : Game
    {
        GraphicsDeviceManager graphics;
        SpriteBatch spriteBatch;
        Texture2D rect;
        SpriteFont font;
 
        List<int> primeNumbers;
        int itemsPerRow;

        int boxWidth;
        int boxHeight;

        int maxNum = 3000;

        public SieveOfEratosthenes()
        {
            graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";
        }

        protected override void Initialize()
        {
            // TODO: Add your initialization logic here
            graphics.PreferredBackBufferWidth = 1440;
            graphics.PreferredBackBufferHeight = 900;
            graphics.ApplyChanges();

            primeNumbers = new List<int>();
            sieveOfEratosthenes(maxNum, ref primeNumbers);
            for (int i = 0; i < primeNumbers.Count; i++)
                System.Console.Write(primeNumbers[i] + ", ");

            itemsPerRow = (int)Math.Ceiling(Math.Sqrt(maxNum));

            boxWidth = graphics.PreferredBackBufferWidth / itemsPerRow;
            boxHeight = graphics.PreferredBackBufferHeight / itemsPerRow;
            rect = new Texture2D(graphics.GraphicsDevice, boxWidth, boxHeight);
            Color[] data = new Color[boxWidth * boxHeight];
            for (int i = 0; i < data.Length; i++)
                data[i] = Color.Chocolate;

            rect.SetData(data);

            base.Initialize();
        }
        protected override void LoadContent()
        {
            // Create a new SpriteBatch, which can be used to draw textures.
            spriteBatch = new SpriteBatch(GraphicsDevice);
            font = Content.Load<SpriteFont>("PrimeNumbers");
            // TODO: use this.Content to load your game content here
        }
        protected override void UnloadContent()
        {
            // TODO: Unload any non ContentManager content here
        }
        protected override void Update(GameTime gameTime)
        {
            if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed || Keyboard.GetState().IsKeyDown(Keys.Escape))
                Exit();

            // TODO: Add your update logic here

            base.Update(gameTime);
        }

        protected override void Draw(GameTime gameTime)
        {
            GraphicsDevice.Clear(Color.CornflowerBlue);
            spriteBatch.Begin();
            int counter = 0;
            for(int i = 0; i < itemsPerRow; i++)
            {
                for(int j = 0; j < itemsPerRow; j++)
                {
                    counter++;
                    string szNum = counter.ToString();
                    spriteBatch.Draw(rect, new Vector2(j * boxWidth, i * boxHeight), (primeNumbers.Contains(counter) ? Color.Green:Color.Red));
                    // spriteBatch.DrawString(font, szNum, new Vector2((j * boxWidth) + ((boxWidth / 2) - (font.MeasureString(szNum).X / 2)), (i * boxHeight) + ((boxHeight / 2) - (font.MeasureString(szNum).Y) / 2)), Color.Black, 0.0f, new Vector2((font.MeasureString(szNum).X / 2 * (float)Math.Pow((float)itemsPerRow / 10.0f, -1) - font.MeasureString(szNum).X / 2), (font.MeasureString(szNum).Y / 2 * (float)Math.Pow((float)itemsPerRow / 10.0f, -1) - font.MeasureString(szNum).Y / 2)), (float)Math.Pow((float)itemsPerRow / 10.0f, -1), SpriteEffects.None, 0.0f);
                    spriteBatch.DrawString(font, szNum, new Vector2(j * boxWidth, i * boxHeight), Color.Black, 0.0f, new Vector2(0, 0), (float)Math.Pow((float)itemsPerRow / 10.0f, -1), SpriteEffects.None, 0.0f);
                }
            }
            
            spriteBatch.End();
            base.Draw(gameTime);
        }

        void sieveOfEratosthenes(int pMaxNum, ref List<int> pPrimeNumbers)
        {

            int max = (int)Math.Ceiling(Math.Sqrt(pMaxNum));

            for (int i = 2; i <= pMaxNum; i++)
            {
                bool found = false;
                for (int j = 2; j < i; j++)
                {
                    double quotient = (float)i / (float)j;
                    int roundedNum = (int)Math.Round(quotient);
                    if ((float)roundedNum == quotient)
                    {
                        found = true;
                        break;
                    }
                }
                if (!found)
                    pPrimeNumbers.Add(i);
            }
        }
    }
}
